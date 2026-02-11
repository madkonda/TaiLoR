#!/usr/bin/env python3
"""
SAM2 Segmentation Service
Processes video frames with SAM2 and saves results as NPZ files
"""
import os

# If using Apple MPS, fall back to CPU for unsupported ops
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

import numpy as np
import torch
from PIL import Image
import cv2
from pathlib import Path
import tempfile
import shutil
from typing import Dict, List, Tuple, Optional
import json
import sys
from contextlib import contextmanager

from googleapiclient.http import MediaFileUpload

# Add SAM2 to path if needed (for GCP VM setup)
_SAM2_BASE_DIR = os.environ.get('SAM2_BASE_DIR', os.path.expanduser('~/sam2'))
_SAM2_BASE_DIR = os.path.expanduser(_SAM2_BASE_DIR)
if os.path.exists(_SAM2_BASE_DIR) and _SAM2_BASE_DIR not in sys.path:
    sys.path.insert(0, _SAM2_BASE_DIR)

# =========================
# Device setup
# =========================
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"Using CUDA device: {torch.cuda.get_device_name(0)}")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
    print("Using Apple Metal Performance Shaders (MPS)")
else:
    device = torch.device("cpu")
    print("Using CPU (slow - consider using GPU)")

print(f"Device: {device}")

if device.type == "cuda":
    torch.autocast("cuda", dtype=torch.bfloat16).__enter__()
    if torch.cuda.get_device_properties(0).major >= 8:
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
elif device.type == "mps":
    print(
        "\nSupport for MPS devices is preliminary. SAM 2 is trained with CUDA and might "
        "give numerically different outputs and sometimes degraded performance on MPS. "
        "See e.g. https://github.com/pytorch/pytorch/issues/84936 for a discussion."
    )

# Import SAM2 (adjust path as needed)
try:
    from sam2.build_sam import build_sam2_video_predictor
except ImportError:
    print("ERROR: SAM2 not found. Please install SAM2 and set up the environment.")
    print("See: https://github.com/facebookresearch/segment-anything-2")
    raise

# Global predictor (load once, reuse)
_predictor = None
_model_cfg = None

# SAM2 paths - adjust for your installation
# For GCP VM with SAM2 at ~/sam2, use absolute or relative paths
_DEFAULT_CHECKPOINT = os.path.join(_SAM2_BASE_DIR, 'checkpoints', 'sam2.1_hiera_large.pt')

# Hydra expects config names relative to the package (as in official notebook)
_DEFAULT_CONFIG_NAME = 'configs/sam2.1/sam2.1_hiera_l.yaml'
_CONFIG_SEARCH_PATHS = [
    os.path.join(_SAM2_BASE_DIR, _DEFAULT_CONFIG_NAME),
    os.path.join(_SAM2_BASE_DIR, 'sam2', _DEFAULT_CONFIG_NAME)
]

def _resolve_config(config_path: Optional[str]) -> Tuple[str, str]:
    """
    Returns a tuple of (config_name_for_hydra, filesystem_path_for_validation).
    If config_path is None, use default. If absolute, validate directly.
    """
    if config_path is None:
        for candidate in _CONFIG_SEARCH_PATHS:
            if os.path.exists(candidate):
                return _DEFAULT_CONFIG_NAME, candidate
        raise FileNotFoundError(
            "SAM2 default config not found. Checked: " + ', '.join(_CONFIG_SEARCH_PATHS)
        )

    if os.path.isabs(config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"SAM2 config not found at {config_path}")
        # Try to convert to relative name when inside repo, otherwise keep absolute
        try:
            rel = os.path.relpath(config_path, _SAM2_BASE_DIR)
            if not rel.startswith('..'):
                return rel, config_path
        except ValueError:
            pass
        return config_path, config_path

    # Relative path provided – validate against repo locations
    candidates = [
        os.path.join(_SAM2_BASE_DIR, config_path),
        os.path.join(_SAM2_BASE_DIR, 'sam2', config_path)
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return config_path, candidate

    raise FileNotFoundError(
        f"SAM2 config not found for '{config_path}'. Checked: {', '.join(candidates)}"
    )


@contextmanager
def _sam2_repo_context():
    """Temporarily chdir into SAM2 repo so Hydra can locate configs."""
    previous_cwd = os.getcwd()
    try:
        os.chdir(_SAM2_BASE_DIR)
        yield
    finally:
        os.chdir(previous_cwd)

def load_sam2_predictor(checkpoint_path: Optional[str] = None,
                       config_path: Optional[str] = None):
    """Load SAM2 predictor model"""
    global _predictor, _model_cfg
    
    if _predictor is not None:
        return _predictor
    
    # Use defaults if not provided
    if checkpoint_path is None:
        checkpoint_path = _DEFAULT_CHECKPOINT

    checkpoint_path = os.path.expanduser(checkpoint_path)
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(
            f"SAM2 checkpoint not found at {checkpoint_path}. "
            f"Looking in: {_SAM2_BASE_DIR}/checkpoints/"
        )

    config_name, config_fs_path = _resolve_config(config_path)

    _model_cfg = config_name
    with _sam2_repo_context():
        _predictor = build_sam2_video_predictor(_model_cfg, checkpoint_path, device=device)
    print(f"SAM2 model loaded from {checkpoint_path}")
    print(f"SAM2 config from {_model_cfg} (fs: {config_fs_path})")
    return _predictor

def process_frames_with_sam2(
    video_dir: str,
    nest_point: Optional[Tuple[float, float]],
    mouse_point: Optional[Tuple[float, float]],
    ann_frame_idx: int = 0,
    nest_obj_id: int = 1,
    mouse_obj_id: int = 2,
    output_npz_path: Optional[str] = None,
    nest_box: Optional[np.ndarray] = None,
    mouse_box: Optional[np.ndarray] = None,
) -> Dict:
    """
    Process video frames with SAM2 segmentation
    
    Args:
        video_dir: Directory containing frames (000000.jpg, 000001.jpg, ...)
        nest_point: (x, y) coordinates for nest point
        mouse_point: (x, y) coordinates for mouse point
        ann_frame_idx: Frame index to annotate (default: 0)
        nest_obj_id: Object ID for nest (default: 1)
        mouse_obj_id: Object ID for mouse (default: 2)
        output_npz_path: Path to save NPZ file (default: video_dir + "_masks.npz")
    
    Returns:
        Dictionary with processing results
    """
    predictor = load_sam2_predictor()
    
    # Get frame list
    frame_names = sorted([
        p for p in os.listdir(video_dir)
        if os.path.splitext(p)[-1].lower() in [".jpg", ".jpeg", ".png"]
    ], key=lambda p: int(os.path.splitext(p)[0]))
    
    if not frame_names:
        raise ValueError(f"No frames found in {video_dir}")
    
    print(f"Processing {len(frame_names)} frames from {video_dir}")
    
    # Initialize predictor state
    inference_state = predictor.init_state(video_path=video_dir)
    predictor.reset_state(inference_state)
    
    # Prompts: either bounding boxes or points (for backwards compatibility)
    # Nest prompt
    if nest_box is not None:
        nest_box_arr = np.asarray(nest_box, dtype=np.float32)
        _, nest_out_obj_ids, nest_out_mask_logits = predictor.add_new_points_or_box(
            inference_state=inference_state,
            frame_idx=ann_frame_idx,
            obj_id=nest_obj_id,
            box=nest_box_arr,
            points=None,
            labels=None,
        )
    else:
        if nest_point is None:
            raise ValueError("Either nest_point or nest_box must be provided for SAM2.")
        nest_points = np.array([[nest_point[0], nest_point[1]]], dtype=np.float32)
        nest_labels = np.array([1], dtype=np.int32)  # 1 = positive
        _, nest_out_obj_ids, nest_out_mask_logits = predictor.add_new_points_or_box(
            inference_state=inference_state,
            frame_idx=ann_frame_idx,
            obj_id=nest_obj_id,
            box=None,
            points=nest_points,
            labels=nest_labels,
        )

    # Mouse prompt
    if mouse_box is not None:
        mouse_box_arr = np.asarray(mouse_box, dtype=np.float32)
        _, mouse_out_obj_ids, mouse_out_mask_logits = predictor.add_new_points_or_box(
            inference_state=inference_state,
            frame_idx=ann_frame_idx,
            obj_id=mouse_obj_id,
            box=mouse_box_arr,
            points=None,
            labels=None,
        )
    else:
        if mouse_point is None:
            raise ValueError("Either mouse_point or mouse_box must be provided for SAM2.")
        mouse_points = np.array([[mouse_point[0], mouse_point[1]]], dtype=np.float32)
        mouse_labels = np.array([1], dtype=np.int32)
        _, mouse_out_obj_ids, mouse_out_mask_logits = predictor.add_new_points_or_box(
            inference_state=inference_state,
            frame_idx=ann_frame_idx,
            obj_id=mouse_obj_id,
            box=None,
            points=mouse_points,
            labels=mouse_labels,
        )
    
    print(f"Added prompts: nest (obj_id={nest_obj_id}), mouse (obj_id={mouse_obj_id})")
    
    # Propagate segmentation through video
    video_segments = {}
    for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
        video_segments[out_frame_idx] = {
            out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
            for i, out_obj_id in enumerate(out_obj_ids)
        }
    
    # Remove annotation frame if present
    if ann_frame_idx in video_segments:
        del video_segments[ann_frame_idx]
    
    print(f"Propagated to {len(video_segments)} frames")
    
    # Determine output path
    if output_npz_path is None:
        video_name = os.path.basename(video_dir.rstrip('/'))
        output_npz_path = os.path.join(
            os.path.dirname(video_dir),
            f"{video_name}_masks.npz"
        )
    
    # Save masks to NPZ
    np.savez_compressed(
        output_npz_path,
        **{
            f"frame{f}_obj{o}": mask
            for f, objs in video_segments.items()
            for o, mask in objs.items()
        }
    )
    
    print(f"[OK] Saved masks to {output_npz_path}")
    
    return {
        "output_path": output_npz_path,
        "num_frames_processed": len(video_segments),
        "num_frames_total": len(frame_names),
        "nest_obj_id": nest_obj_id,
        "mouse_obj_id": mouse_obj_id
    }

def download_frames_from_drive(
    drive_service,
    folder_id: str,
    local_dir: str
) -> List[str]:
    """
    Download frames from Google Drive folder to local directory
    
    Args:
        drive_service: Google Drive API service object
        folder_id: Google Drive folder ID containing frames
        local_dir: Local directory to save frames
    
    Returns:
        List of local frame file paths
    """
    os.makedirs(local_dir, exist_ok=True)
    
    # List ALL files in Drive folder with pagination
    files = []
    page_token = None
    
    while True:
        request_params = {
            'q': f"'{folder_id}' in parents and mimeType='image/jpeg' and trashed=false",
            'fields': "nextPageToken, files(id, name)",
            'orderBy': 'name',  # Order by name to ensure consistent sorting
            'pageSize': 1000  # Max page size
        }
        if page_token:
            request_params['pageToken'] = page_token
        
        results = drive_service.files().list(**request_params).execute()
        
        files.extend(results.get('files', []))
        page_token = results.get('nextPageToken')
        
        if not page_token:
            break
    
    if not files:
        raise ValueError(f"No frames found in Drive folder {folder_id}")
    
    # Sort by filename (should be 000000.jpg, 000001.jpg, etc.)
    files.sort(key=lambda f: f['name'])
    
    print(f"Found {len(files)} frames in Drive folder")
    
    local_paths = []
    for file_info in files:
        local_path = os.path.join(local_dir, file_info['name'])
        
        # Download file
        request = drive_service.files().get_media(fileId=file_info['id'])
        with open(local_path, 'wb') as f:
            f.write(request.execute())
        
        local_paths.append(local_path)
        print(f"Downloaded: {file_info['name']}")
    
    print(f"Downloaded {len(local_paths)} frames to {local_dir}")
    return local_paths

def upload_file_to_drive(
    drive_service,
    source_path: str,
    parent_folder_id: str,
    filename: Optional[str] = None,
    mime_type: str = 'application/octet-stream'
) -> Dict:
    """
    Upload a file to Google Drive
    
    Args:
        drive_service: Google Drive API service object
        source_path: Local path to file
        parent_folder_id: Google Drive folder ID to upload to
        filename: Optional custom filename (default: basename of npz_path)
        mime_type: MIME type of the file being uploaded
    
    Returns:
        Dictionary with file metadata
    """
    source_path = os.path.abspath(os.path.expanduser(source_path))
    
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Cannot upload: file does not exist at {source_path}")
    
    file_size = os.path.getsize(source_path)
    print(f"Uploading {os.path.basename(source_path)} ({file_size} bytes) to Drive folder {parent_folder_id}")
    
    if filename is None:
        filename = os.path.basename(source_path)
    
    file_metadata = {
        'name': filename,
        'parents': [parent_folder_id],
        'mimeType': mime_type
    }
    
    try:
        # Use resumable upload for better reliability
        # Google API client handles resumable uploads automatically with retries
        # chunksize of 256KB is a good balance for network reliability
        media = MediaFileUpload(
            source_path, 
            mimetype=mime_type, 
            resumable=True,
            chunksize=256*1024  # 256KB chunks
        )
        
        # Initiate the resumable upload
        request = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        )
        
        # Execute the upload - next_chunk() handles chunking and retries automatically
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                progress = int(status.progress() * 100)
                print(f"[UPLOAD] Progress: {progress}%")
        
        if not response:
            raise RuntimeError("Upload failed: no response received")
        
        web_link = response.get('webViewLink', 'N/A')
        file_id = response.get('id', 'N/A')
        print(f"[OK] Uploaded {filename} to Drive (ID: {file_id}, Link: {web_link})")
        return response
    except Exception as e:
        print(f"[ERROR] Failed to upload {filename} to Drive: {str(e)}")
        import traceback
        print(f"[ERROR] Traceback: {traceback.format_exc()}")
        raise

if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 5:
        print("Usage: python sam2_service.py <video_dir> <nest_x> <nest_y> <mouse_x> <mouse_y> [ann_frame_idx]")
        sys.exit(1)
    
    video_dir = sys.argv[1]
    nest_point = (float(sys.argv[2]), float(sys.argv[3]))
    mouse_point = (float(sys.argv[4]), float(sys.argv[5]))
    ann_frame_idx = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    
    result = process_frames_with_sam2(
        video_dir=video_dir,
        nest_point=nest_point,
        mouse_point=mouse_point,
        ann_frame_idx=ann_frame_idx
    )
    
    print(json.dumps(result, indent=2))

