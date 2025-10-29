#!/usr/bin/env python3
"""
TaiLOR Video Processing Pipeline
- Extracts frames using ffmpeg (every 10th frame at 30fps)
- Processes frames with SAM2 for mouse/nest segmentation
- Accepts parameters from frontend
"""

import os
import sys
import subprocess
import argparse
import json
from pathlib import Path

# if using Apple MPS, fall back to CPU for unsupported ops
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
import numpy as np
import torch
import matplotlib.pyplot as plt
from PIL import Image
import csv
import cv2
from math import sqrt

def extract_frames(video_path, output_dir, fps=30, every_nth=10):
    """
    Extract frames from video using ffmpeg
    Args:
        video_path: Path to input video
        output_dir: Directory to save frames
        fps: Video frame rate
        every_nth: Extract every nth frame
    """
    print(f"🎬 Extracting frames from {video_path}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Calculate frame interval (every 10th frame at 30fps = every 0.33 seconds)
    frame_interval = every_nth / fps
    
    # FFmpeg command to extract frames
    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'fps=1/{frame_interval}',  # Extract every nth frame
        '-q:v', '2',  # High quality
        os.path.join(output_dir, '%06d.jpg')
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Frames extracted successfully to {output_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error extracting frames: {e}")
        print(f"FFmpeg stderr: {e.stderr}")
        return False

def setup_device():
    """Setup PyTorch device"""
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print(f"using device: {device}")

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
    
    return device

def show_mask(mask, ax, obj_id=None, random_color=False):
    """Display mask on axis"""
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        cmap = plt.get_cmap("tab10")
        cmap_idx = 0 if obj_id is None else obj_id
        color = np.array([*cmap(cmap_idx)[:3], 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

def show_points(coords, labels, ax, marker_size=375):
    """Display points on axis"""
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)

def show_box(box, ax):
    """Display bounding box on axis"""
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))

def process_video_with_sam2(video_path, frames_dir, nest_coords, mouse_coords, output_dir):
    """
    Process video with SAM2 segmentation
    Args:
        video_path: Path to original video
        frames_dir: Directory containing extracted frames
        nest_coords: [x, y] coordinates for nest
        mouse_coords: [x, y] coordinates for mouse
        output_dir: Directory to save results
    """
    print(f"🔬 Starting SAM2 processing...")
    
    # Setup device
    device = setup_device()
    
    # Import SAM2 (assuming it's installed)
    try:
        from sam2.build_sam import build_sam2_video_predictor
    except ImportError:
        print("❌ SAM2 not found. Please install SAM2 first.")
        return False
    
    # SAM2 configuration
    sam2_checkpoint = "../checkpoints/sam2.1_hiera_large.pt"
    model_cfg = "configs/sam2.1/sam2.1_hiera_l.yaml"
    
    # Check if checkpoint exists
    if not os.path.exists(sam2_checkpoint):
        print(f"❌ SAM2 checkpoint not found: {sam2_checkpoint}")
        return False
    
    # Initialize predictor
    predictor = build_sam2_video_predictor(model_cfg, sam2_checkpoint, device=device)
    
    # Get frame names
    frame_names = [
        p for p in os.listdir(frames_dir)
        if os.path.splitext(p)[-1].lower() in [".jpg", ".jpeg"]
    ]
    frame_names.sort(key=lambda p: int(os.path.splitext(p)[0]))
    
    print(f"📁 Frames dir: {frames_dir} | #frames = {len(frame_names)}")
    
    # Initialize predictor state
    inference_state = predictor.init_state(video_path=frames_dir)
    predictor.reset_state(inference_state)
    
    # Add prompts via points
    ann_frame_idx = 0
    nest_obj_id = 1
    mouse_obj_id = 2
    
    # Convert coordinates to numpy arrays
    nest_points = np.array([nest_coords], dtype=np.float32)
    nest_labels = np.array([1], dtype=np.int32)
    
    mouse_points = np.array([mouse_coords], dtype=np.float32)
    mouse_labels = np.array([1], dtype=np.int32)
    
    print(f"🎯 Nest coordinates: {nest_coords}")
    print(f"🐭 Mouse coordinates: {mouse_coords}")
    
    # Add points for the nest
    _, nest_out_obj_ids, nest_out_mask_logits = predictor.add_new_points_or_box(
        inference_state=inference_state,
        frame_idx=ann_frame_idx,
        obj_id=nest_obj_id,
        box=None,
        points=nest_points,
        labels=nest_labels
    )
    
    # Add points for the mouse
    _, mouse_out_obj_ids, mouse_out_mask_logits = predictor.add_new_points_or_box(
        inference_state=inference_state,
        frame_idx=ann_frame_idx,
        obj_id=mouse_obj_id,
        box=None,
        points=mouse_points,
        labels=mouse_labels
    )
    
    # Propagate segmentation through video
    print("🔄 Propagating segmentation through video...")
    video_segments = {}
    for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
        video_segments[out_frame_idx] = {
            out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
            for i, out_obj_id in enumerate(out_obj_ids)
        }
    
    if 0 in video_segments:
        del video_segments[0]
    
    print(f"✅ Propagated frames: {len(video_segments)}")
    
    # Save masks to NPZ
    os.makedirs(output_dir, exist_ok=True)
    video_name = Path(video_path).stem
    mask_file = os.path.join(output_dir, f"{video_name}_mouse_masks.npz")
    
    np.savez_compressed(
        mask_file,
        **{
            f"frame{f}_obj{o}": mask
            for f, objs in video_segments.items()
            for o, mask in objs.items()
        }
    )
    print(f"💾 Saved all masks to {mask_file}")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Process video with SAM2 segmentation')
    parser.add_argument('--video_path', required=True, help='Path to input video')
    parser.add_argument('--nest_x', type=int, required=True, help='Nest X coordinate')
    parser.add_argument('--nest_y', type=int, required=True, help='Nest Y coordinate')
    parser.add_argument('--mouse_x', type=int, required=True, help='Mouse X coordinate')
    parser.add_argument('--mouse_y', type=int, required=True, help='Mouse Y coordinate')
    parser.add_argument('--output_dir', default='./results', help='Output directory')
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Get video name for frames directory
    video_name = Path(args.video_path).stem
    frames_dir = os.path.join(args.output_dir, video_name)
    
    print(f"🚀 Starting video processing pipeline")
    print(f"📹 Video: {args.video_path}")
    print(f"📁 Frames will be saved to: {frames_dir}")
    print(f"📊 Output directory: {args.output_dir}")
    
    # Step 1: Extract frames
    if not extract_frames(args.video_path, frames_dir):
        print("❌ Frame extraction failed")
        return 1
    
    # Step 2: Process with SAM2
    nest_coords = [args.nest_x, args.nest_y]
    mouse_coords = [args.mouse_x, args.mouse_y]
    
    if not process_video_with_sam2(args.video_path, frames_dir, nest_coords, mouse_coords, args.output_dir):
        print("❌ SAM2 processing failed")
        return 1
    
    print("✅ Video processing completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
