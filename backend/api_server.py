#!/usr/bin/env python3
"""Flask API server for SAM2 segmentation service."""

from __future__ import annotations

import json
import os
import tempfile
import threading
import time
import uuid
from pathlib import Path
from typing import Dict, Tuple, List, Sequence, Any

import numpy as np

from flask import Flask, jsonify, request
from flask_cors import CORS
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from sam2_service import (
    download_frames_from_drive,
    process_frames_with_sam2,
    upload_file_to_drive,
)

from mouse_extraction import (
    DEFAULT_FIXED_POINTS as DEFAULT_MOUSE_POINTS,
    extract_mouse_features,
)
from rat_extraction import (
    DEFAULT_FIXED_POINTS as DEFAULT_RAT_POINTS,
    extract_rat_features,
)
from rat2_extraction import (
    DEFAULT_FIXED_POINTS as DEFAULT_RAT_ONLY_POINTS,
    extract_rat_only_features,
)
from prediction import run_prediction
from review_flags import generate_review_flags, ReviewStats

BACKEND_DIR = Path(__file__).resolve().parent
ROOT_DIR = BACKEND_DIR.parent
FOLDER_MIME = 'application/vnd.google-apps.folder'

# In-memory job store for async processing
_JOBS: Dict[str, Dict[str, Any]] = {}
_JOBS_LOCK = threading.Lock()


def _ensure_subfolder(drive_service, parent_id: str, name: str) -> Tuple[str, str | None]:
    escaped_name = name.replace("'", "\\'")
    query = (
        f"'{parent_id}' in parents and name = '{escaped_name}' "
        f"and mimeType = '{FOLDER_MIME}' and trashed = false"
    )
    result = drive_service.files().list(
        q=query,
        fields='files(id,name,webViewLink)',
        pageSize=1
    ).execute().get('files', [])

    if result:
        folder = result[0]
        return folder['id'], folder.get('webViewLink')

    metadata = {
        'name': name,
        'mimeType': FOLDER_MIME,
        'parents': [parent_id],
    }
    created = drive_service.files().create(
        body=metadata,
        fields='id,webViewLink'
    ).execute()
    return created['id'], created.get('webViewLink')


def _list_files_in_folder(drive_service, folder_id: str, fields: str = 'files(id,name)') -> List[Dict]:
    items: List[Dict] = []
    page_token = None
    while True:
        response = drive_service.files().list(
            q=f"'{folder_id}' in parents and trashed = false",
            fields=f'nextPageToken,{fields}',
            pageSize=1000,
            pageToken=page_token
        ).execute()
        items.extend(response.get('files', []))
        page_token = response.get('nextPageToken')
        if not page_token:
            break
    return items


def _clear_folder(drive_service, folder_id: str) -> None:
    files = _list_files_in_folder(drive_service, folder_id, fields='files(id)')
    for file_info in files:
        try:
            drive_service.files().delete(fileId=file_info['id']).execute()
        except Exception as exc:  # pragma: no cover - best effort cleanup
            print(f"[WARN] Failed to delete old watch file {file_info['id']}: {exc}")


def _collect_flagged_frame_names(flagged_indices: Sequence[int]) -> List[str]:
    names = sorted({f"{idx:06d}.jpg" for idx in flagged_indices})
    return names


def _copy_frames_to_watch(
    drive_service,
    video_folder_id: str,
    flagged_indices: Sequence[int],
) -> Tuple[int, int, str, str | None]:
    """Copy flagged frames into a `watch` subfolder.

    Returns a tuple of (requested_count, copied_count, watch_folder_id, watch_folder_link).
    """

    watch_folder_id, watch_link = _ensure_subfolder(drive_service, video_folder_id, 'watch')
    _clear_folder(drive_service, watch_folder_id)

    frames_folder = drive_service.files().list(
        q=(
            f"'{video_folder_id}' in parents and name = 'frames' and "
            f"mimeType = '{FOLDER_MIME}' and trashed = false"
        ),
        fields='files(id,name)',
        pageSize=1
    ).execute().get('files', [])

    if not frames_folder:
        return len(flagged_indices), 0, watch_folder_id, watch_link

    frame_folder_id = frames_folder[0]['id']
    frame_files = _list_files_in_folder(drive_service, frame_folder_id, fields='files(id,name)')
    frame_lookup = {item['name']: item['id'] for item in frame_files}

    flagged_names = _collect_flagged_frame_names(flagged_indices)
    copied = 0

    for name in flagged_names:
        file_id = frame_lookup.get(name)
        if not file_id:
            continue
        body = {
            'name': name,
            'parents': [watch_folder_id],
        }
        try:
            drive_service.files().copy(fileId=file_id, body=body, fields='id').execute()
            copied += 1
        except Exception as exc:  # pragma: no cover
            print(f"[WARN] Failed to copy frame {name} to watch folder: {exc}")

    return len(flagged_names), copied, watch_folder_id, watch_link


def _resolve_tree_logic_path(filename: str) -> Path:
    for base in (BACKEND_DIR, ROOT_DIR):
        candidate = base / filename
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"tree_logic file not found: {filename}")


TEMPLATE_CONFIGS: Dict[str, Dict] = {
    "mouse_less_nest": {
        "extractor": "mouse",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "mouse_less_nest.json",
        "tree_logic_file": "mouse_less_nest_tree_logic.py",
        "nest_object_id": 1,
        "mouse_object_id": 2,
    },
    "mouse_nest": {
        "extractor": "mouse",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "mouse_nest.json",
        "tree_logic_file": "mouse_nest_tree_logic.py",
        "nest_object_id": 1,
        "mouse_object_id": 2,
    },
    "rat1": {
        "extractor": "rat",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "rat1.json",
        "tree_logic_file": "rat1_tree_logic.py",
        "rat_object_id": 2,
        "nest_object_id": 1,
    },
    "rat2": {
        "extractor": "rat_only",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "rat2.json",
        "tree_logic_file": "rat2_tree_logic.py",
        "rat_only_object_id": 1,
    },
    "rat3": {
        "extractor": "rat",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "rat3.json",
        "tree_logic_file": "rat3_tree_logic.py",
        "rat_object_id": 2,
        "nest_object_id": 1,
    },
    "rat4": {
        "extractor": "rat",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "rat4.json",
        "tree_logic_file": "rat4_tree_logic.py",
        "rat_object_id": 2,
        "nest_object_id": 1,
    },
    "rat5": {
        "extractor": "rat",
        "fixed_points_file": BACKEND_DIR / "fixed_points_configs" / "rat5.json",
        "tree_logic_file": "rat5_tree_logic.py",
        "rat_object_id": 2,
        "nest_object_id": 1,
    },
}


app = Flask(__name__)

_cors_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
_cors_extra = os.environ.get("CORS_ORIGINS", "")
if _cors_extra:
    _cors_origins.extend(o.strip() for o in _cors_extra.split(",") if o.strip())
CORS(
    app,
    resources={
        r"/*": {
            "origins": _cors_origins,
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "POST", "OPTIONS"],
        }
    },
)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


def _coerce_fixed_points(raw: Dict) -> Dict[str, Tuple[int, int]]:
    coerced: Dict[str, Tuple[int, int]] = {}
    for key, value in raw.items():
        if isinstance(value, dict) and 'x' in value and 'y' in value:
            coerced[key] = (int(value['x']), int(value['y']))
        elif isinstance(value, (list, tuple)) and len(value) >= 2:
            coerced[key] = (int(value[0]), int(value[1]))
    return coerced


def _load_fixed_points_file(path: Path) -> Dict[str, Tuple[int, int]]:
    with path.open('r', encoding='utf-8') as fh:
        data = json.load(fh)
    if isinstance(data, dict) and 'fixed_points' in data:
        data = data['fixed_points']
    if not isinstance(data, dict):
        raise ValueError(f'Invalid fixed points file: {path}')
    return _coerce_fixed_points(data)


def _apply_template(
    template_key: str | None,
    analysis_type: str,
    fixed_points_payload: Dict | None,
    nest_object_id: int,
    mouse_object_id: int,
    rat_object_id: int,
    rat_only_object_id: int
) -> Tuple[str, Dict[str, Tuple[int, int]] | None, Path | None, int, int, int, int]:
    fixed_points: Dict[str, Tuple[int, int]] | None = None
    tree_logic_path: Path | None = None

    if template_key:
        normalized = str(template_key).lower().replace('.json', '')
        template_cfg = TEMPLATE_CONFIGS.get(normalized)
        if not template_cfg:
            raise ValueError(f'Unknown fixed points template: {template_key}')

        analysis_type = template_cfg['extractor']
        fixed_points = _load_fixed_points_file(template_cfg['fixed_points_file'])
        tree_logic_path = _resolve_tree_logic_path(template_cfg['tree_logic_file'])

        nest_object_id = template_cfg.get('nest_object_id', nest_object_id)
        mouse_object_id = template_cfg.get('mouse_object_id', mouse_object_id)
        rat_object_id = template_cfg.get('rat_object_id', rat_object_id)
        rat_only_object_id = template_cfg.get('rat_only_object_id', rat_only_object_id)

    if isinstance(fixed_points_payload, dict) and fixed_points_payload:
        coerced = _coerce_fixed_points(fixed_points_payload)
        if coerced:
            fixed_points = coerced

    return (
        analysis_type,
        fixed_points,
        tree_logic_path,
        nest_object_id,
        mouse_object_id,
        rat_object_id,
        rat_only_object_id,
    )


def _process_npz_outputs(
    npz_path: str,
    analysis_type: str,
    fixed_points: Dict[str, Tuple[int, int]] | None,
    nest_object_id: int,
    mouse_object_id: int,
    rat_object_id: int,
    rat_only_object_id: int,
    drive_service,
    video_folder_id: str,
    tree_logic_path: Path | None,
) -> Dict[str, str]:
    if analysis_type == 'rat_only':
        csv_path = extract_rat_only_features(
            npz_path,
            fixed_points=fixed_points or DEFAULT_RAT_ONLY_POINTS,
            rat_id=rat_only_object_id,
        )
    elif analysis_type == 'rat':
        csv_path = extract_rat_features(
            npz_path,
            fixed_points=fixed_points or DEFAULT_RAT_POINTS,
            rat_id=rat_object_id,
            nest_id=nest_object_id,
        )
    else:
        csv_path = extract_mouse_features(
            npz_path,
            fixed_points=fixed_points or DEFAULT_MOUSE_POINTS,
            nest_id=nest_object_id,
            mouse_id=mouse_object_id,
        )

    uploaded_csv = upload_file_to_drive(
        drive_service,
        csv_path,
        video_folder_id,
        filename=os.path.basename(csv_path),
        mime_type='text/csv',
    )

    result: Dict[str, str] = {
        'csv_drive_id': uploaded_csv.get('id', ''),
        'csv_drive_link': uploaded_csv.get('webViewLink', ''),
    }

    if tree_logic_path:
        prediction_output = run_prediction(Path(csv_path), tree_logic_path)
        uploaded_prediction = upload_file_to_drive(
            drive_service,
            str(prediction_output),
            video_folder_id,
            filename=os.path.basename(prediction_output),
            mime_type='text/csv',
        )
        result['prediction_drive_id'] = uploaded_prediction.get('id', '')
        result['prediction_drive_link'] = uploaded_prediction.get('webViewLink', '')

    return result


def _create_job(initial_payload: Dict[str, Any] | None = None) -> str:
    """Create a new job entry and return its ID."""
    job_id = str(uuid.uuid4())
    now = time.time()
    with _JOBS_LOCK:
        _JOBS[job_id] = {
            "id": job_id,
            "status": "queued",
            "created_at": now,
            "updated_at": now,
            "progress": {"stage": "queued"},
            "result": None,
            "error": None,
            "traceback": None,
        }
        if initial_payload:
            _JOBS[job_id]["request"] = initial_payload
    return job_id


def _update_job(job_id: str, **fields: Any) -> None:
    """Update a job entry in a threadsafe way."""
    with _JOBS_LOCK:
        job = _JOBS.get(job_id)
        if not job:
            return
        job.update(fields)
        job["updated_at"] = time.time()


def _run_process_sam2_job(job_id: str, payload: Dict[str, Any]) -> None:
    """Background worker for SAM2 processing."""
    try:
        _update_job(job_id, status="running", progress={"stage": "initializing"})

        access_token = payload.get('access_token')
        frame_folder_id = payload.get('frame_folder_id')
        frame_folder_name = payload.get('frame_folder_name')  # NEW: local folder name
        video_folder_id = payload.get('video_folder_id')
        nest_point = payload.get('nest_point')
        mouse_point = payload.get('mouse_point')
        ann_frame_idx = payload.get('ann_frame_idx', 0)
        analysis_type_initial = (payload.get('analysis_type') or 'mouse').lower()
        fixed_points_payload = payload.get('fixed_points') or {}
        template_key_raw = payload.get('fixed_points_template')
        run_prediction_flag = bool(payload.get('run_prediction'))
        nest_object_id = payload.get('nest_object_id', 1)
        mouse_object_id = payload.get('mouse_object_id', 2)
        rat_object_id = payload.get('rat_object_id', 2)
        rat_only_object_id = payload.get('rat_only_object_id', 1)
        nest_box_payload = payload.get('nest_box')
        mouse_box_payload = payload.get('mouse_box')

        (
            analysis_type,
            fixed_points,
            tree_logic_path,
            nest_object_id,
            mouse_object_id,
            rat_object_id,
            rat_only_object_id,
        ) = _apply_template(
            template_key_raw,
            analysis_type_initial,
            fixed_points_payload,
            nest_object_id,
            mouse_object_id,
            rat_object_id,
            rat_only_object_id,
        )

        # Require either frame_folder_id (Drive) or frame_folder_name (local)
        if not frame_folder_id and not frame_folder_name:
            raise ValueError(
                'Missing required parameter: either frame_folder_id (Drive) or frame_folder_name (local) must be provided'
            )

        if not access_token:
            raise ValueError('Missing required parameter: access_token')

        # Require either both points or both boxes
        has_points = bool(nest_point and mouse_point)
        has_boxes = bool(nest_box_payload and mouse_box_payload)
        if not (has_points or has_boxes):
            raise ValueError(
                'You must provide either both nest_point and mouse_point, or both nest_box and mouse_box.'
            )

        creds = Credentials(token=access_token)
        drive_service = build('drive', 'v3', credentials=creds)

        _update_job(job_id, progress={"stage": "resolving_video_folder"})

        # If using local frames, video_folder_id must be provided directly
        if frame_folder_name:
            if not video_folder_id:
                raise ValueError(
                    'When using frame_folder_name (local frames), video_folder_id must be provided to upload NPZ to Drive.'
                )
            # Use local path directly
            local_videos_dir = os.path.join(BACKEND_DIR, 'videos')
            video_dir = os.path.join(local_videos_dir, frame_folder_name)
            if not os.path.exists(video_dir):
                raise ValueError(f'Local frame folder not found: {video_dir}')
            
            # Get video folder name from Drive for NPZ filename
            video_info = drive_service.files().get(
                fileId=video_folder_id, fields='name'
            ).execute()
            video_folder_name = video_info.get('name', 'video')
            video_base = os.path.splitext(video_folder_name)[0]
            
            # Use temp dir for NPZ output
            with tempfile.TemporaryDirectory() as temp_dir:
                npz_path = os.path.join(temp_dir, f'{video_base}.npz')
                
                _update_job(job_id, progress={"stage": "running_sam2"})
                
                # Prepare optional boxes if provided as [x1, y1, x2, y2]
                nest_box = None
                if isinstance(nest_box_payload, (list, tuple)) and len(nest_box_payload) == 4:
                    nest_box = np.array(nest_box_payload, dtype=np.float32)

                mouse_box = None
                if isinstance(mouse_box_payload, (list, tuple)) and len(mouse_box_payload) == 4:
                    mouse_box = np.array(mouse_box_payload, dtype=np.float32)

                nest_coords = (nest_point['x'], nest_point['y']) if nest_point else None
                mouse_coords = (mouse_point['x'], mouse_point['y']) if mouse_point else None

                result = process_frames_with_sam2(
                    video_dir=video_dir,
                    nest_point=nest_coords,
                    mouse_point=mouse_coords,
                    ann_frame_idx=ann_frame_idx,
                    output_npz_path=npz_path,
                    nest_box=nest_box,
                    mouse_box=mouse_box,
                )

                # Verify NPZ file was created
                if not os.path.exists(npz_path):
                    raise FileNotFoundError(
                        f"NPZ file not found at {npz_path} after SAM2 processing"
                    )

                npz_size = os.path.getsize(npz_path)
                print(f"[JOB {job_id}] NPZ file ready for upload: {npz_path} ({npz_size} bytes)")

                # Upload NPZ to Drive
                _update_job(job_id, progress={"stage": "uploading_npz"})
                uploaded_npz = upload_file_to_drive(
                    drive_service,
                    npz_path,
                    video_folder_id,
                    filename=f'{video_base}.npz',
                    mime_type='application/zip',
                )
                result['npz_drive_id'] = uploaded_npz.get('id')
                result['npz_drive_link'] = uploaded_npz.get('webViewLink')

                if run_prediction_flag:
                    _update_job(job_id, progress={"stage": "running_prediction"})
                    outputs = _process_npz_outputs(
                        npz_path,
                        analysis_type,
                        fixed_points,
                        nest_object_id,
                        mouse_object_id,
                        rat_object_id,
                        rat_only_object_id,
                        drive_service,
                        video_folder_id,
                        tree_logic_path,
                    )
                    result.update(outputs)

                _update_job(
                    job_id,
                    status="completed",
                    progress={"stage": "completed"},
                    result=result,
                )
            return  # Early return for local frames path

        # Original Drive download path
        if not video_folder_id:
            parent_info = drive_service.files().get(
                fileId=frame_folder_id, fields='parents'
            ).execute()
            parents = parent_info.get('parents', [])
            if parents:
                video_folder_id = parents[0]
            else:
                raise ValueError('Unable to resolve video folder from frame folder.')

        with tempfile.TemporaryDirectory() as temp_dir:
            _update_job(job_id, progress={"stage": "downloading_frames"})
            frame_paths = download_frames_from_drive(
                drive_service, frame_folder_id, temp_dir
            )
            if not frame_paths:
                raise ValueError('No frames found in Drive folder.')

            nest_coords = (nest_point['x'], nest_point['y']) if nest_point else None
            mouse_coords = (mouse_point['x'], mouse_point['y']) if mouse_point else None

            video_info = drive_service.files().get(
                fileId=video_folder_id, fields='name'
            ).execute()
            video_folder_name = video_info.get('name', 'video')
            video_base = os.path.splitext(video_folder_name)[0]
            npz_path = os.path.join(temp_dir, f'{video_base}.npz')

            _update_job(job_id, progress={"stage": "running_sam2"})

            # Prepare optional boxes if provided as [x1, y1, x2, y2]
            nest_box = None
            if isinstance(nest_box_payload, (list, tuple)) and len(nest_box_payload) == 4:
                nest_box = nest_box_payload

            mouse_box = None
            if isinstance(mouse_box_payload, (list, tuple)) and len(mouse_box_payload) == 4:
                mouse_box = mouse_box_payload

            result = process_frames_with_sam2(
                video_dir=temp_dir,
                nest_point=nest_coords,
                mouse_point=mouse_coords,
                ann_frame_idx=ann_frame_idx,
                output_npz_path=npz_path,
                nest_box=nest_box,
                mouse_box=mouse_box,
            )

            # Verify NPZ file was created
            if not os.path.exists(npz_path):
                raise FileNotFoundError(
                    f"NPZ file not found at {npz_path} after SAM2 processing"
                )

            npz_size = os.path.getsize(npz_path)
            print(f"[JOB {job_id}] NPZ file ready for upload: {npz_path} ({npz_size} bytes)")

            # Upload NPZ to Drive
            _update_job(job_id, progress={"stage": "uploading_npz"})
            uploaded_npz = upload_file_to_drive(
                drive_service,
                npz_path,
                video_folder_id,
                filename=f'{video_base}.npz',
                mime_type='application/zip',
            )
            result['npz_drive_id'] = uploaded_npz.get('id')
            result['npz_drive_link'] = uploaded_npz.get('webViewLink')

            if run_prediction_flag:
                _update_job(job_id, progress={"stage": "running_prediction"})
                outputs = _process_npz_outputs(
                    npz_path,
                    analysis_type,
                    fixed_points,
                    nest_object_id,
                    mouse_object_id,
                    rat_object_id,
                    rat_only_object_id,
                    drive_service,
                    video_folder_id,
                    tree_logic_path,
                )
                result.update(outputs)

        _update_job(
            job_id,
            status="completed",
            progress={"stage": "completed"},
            result=result,
        )
    except Exception as err:  # pragma: no cover - best effort reporting
        import traceback

        _update_job(
            job_id,
            status="failed",
            error=str(err),
            traceback=traceback.format_exc(),
            progress={"stage": "failed"},
        )


@app.route('/process-sam2', methods=['OPTIONS', 'POST'])
def process_sam2():
    try:
        if request.method == 'OPTIONS':
            return ('', 204)

        data = request.json or {}

        # Create job and start background worker
        job_id = _create_job(initial_payload=data)
        worker = threading.Thread(
            target=_run_process_sam2_job, args=(job_id, data), daemon=True
        )
        worker.start()

        return jsonify(
            {
                "job_id": job_id,
                "status": "queued",
            }
        )

    except Exception as err:
        import traceback

        return jsonify({'error': str(err), 'traceback': traceback.format_exc()}), 500


@app.route('/jobs/<job_id>', methods=['GET'])
def get_job_status(job_id: str):
    """Return status for an async job."""
    with _JOBS_LOCK:
        job = _JOBS.get(job_id)
        if not job:
            return jsonify({"error": "Job not found"}), 404

        # Avoid leaking full request payloads in the response
        public_job = {
            key: value
            for key, value in job.items()
            if key not in {"request"}
        }

    return jsonify(public_job)


@app.route('/run-prediction', methods=['OPTIONS', 'POST'])
def run_prediction_endpoint():
    try:
        if request.method == 'OPTIONS':
            return ('', 204)

        data = request.json or {}

        access_token = data.get('access_token')
        video_folder_id = data.get('video_folder_id')
        template_key_raw = data.get('fixed_points_template')
        npz_file_id = data.get('npz_file_id')
        fixed_points_payload = data.get('fixed_points') or {}
        analysis_type_initial = (data.get('analysis_type') or 'mouse').lower()
        nest_object_id = data.get('nest_object_id', 1)
        mouse_object_id = data.get('mouse_object_id', 2)
        rat_object_id = data.get('rat_object_id', 2)
        rat_only_object_id = data.get('rat_only_object_id', 1)

        if not access_token:
            return jsonify({'error': 'Missing access_token'}), 400

        creds = Credentials(token=access_token)
        drive_service = build('drive', 'v3', credentials=creds)

        npz_metadata = None

        if npz_file_id:
            npz_metadata = drive_service.files().get(
                fileId=npz_file_id,
                fields='id,name,parents,webViewLink'
            ).execute()
            if not video_folder_id:
                parents = npz_metadata.get('parents', [])
                if parents:
                    video_folder_id = parents[0]

        if not video_folder_id:
            return jsonify({'error': 'Missing video_folder_id and unable to infer from NPZ file'}), 400

        video_metadata = drive_service.files().get(
            fileId=video_folder_id,
            fields='id,name'
        ).execute()
        video_folder_name = video_metadata.get('name', 'video')
        video_base = os.path.splitext(video_folder_name)[0]

        if npz_metadata is None:
            expected_name = f"{video_base}.npz"
            expected_name_escaped = expected_name.replace("'", "\\'")
            query_expected = (
                f"'{video_folder_id}' in parents and name = '{expected_name_escaped}' and trashed = false"
            )
            candidate = drive_service.files().list(
                q=query_expected,
                fields='files(id,name,webViewLink)',
                pageSize=1
            ).execute().get('files', [])

            if not candidate:
                query_any_npz = (
                    f"'{video_folder_id}' in parents and name contains '.npz' and trashed = false"
                )
                candidate = drive_service.files().list(
                    q=query_any_npz,
                    fields='files(id,name,webViewLink)',
                    orderBy='modifiedTime desc',
                    pageSize=1
                ).execute().get('files', [])

            if not candidate:
                return jsonify({'error': 'No NPZ file found in the selected video folder.'}), 404

            npz_metadata = candidate[0]
            npz_file_id = npz_metadata['id']

        npz_web_link = npz_metadata.get('webViewLink')
        npz_name = npz_metadata.get('name', f'{video_base}.npz')

        (
            analysis_type,
            fixed_points,
            tree_logic_path,
            nest_object_id,
            mouse_object_id,
            rat_object_id,
            rat_only_object_id,
        ) = _apply_template(
            template_key_raw,
            analysis_type_initial,
            fixed_points_payload,
            nest_object_id,
            mouse_object_id,
            rat_object_id,
            rat_only_object_id,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            npz_path = os.path.join(temp_dir, npz_name)
            request_media = drive_service.files().get_media(fileId=npz_file_id)
            with open(npz_path, 'wb') as fh:
                fh.write(request_media.execute())

            outputs = _process_npz_outputs(
                npz_path,
                analysis_type,
                fixed_points,
                nest_object_id,
                mouse_object_id,
                rat_object_id,
                rat_only_object_id,
                drive_service,
                video_folder_id,
                tree_logic_path,
            )

        response_payload = {
            'video_folder_id': video_folder_id,
            'video_name': video_folder_name,
            'npz_drive_id': npz_file_id,
            'npz_drive_link': npz_web_link,
        }
        response_payload.update(outputs)

        return jsonify(response_payload)

    except Exception as err:
        import traceback

        return jsonify({'error': str(err), 'traceback': traceback.format_exc()}), 500


@app.route('/generate-review-flags', methods=['OPTIONS', 'POST'])
def generate_review_flags_endpoint():
    """Generate review flags from a prediction CSV file."""
    try:
        if request.method == 'OPTIONS':
            return ('', 204)

        data = request.json or {}
        access_token = data.get('access_token')
        prediction_csv_file_id = data.get('prediction_csv_file_id')
        fps_video = float(data.get('fps_video', 30.0))
        frame_stride = int(data.get('frame_stride', 10))
        seconds_window = float(data.get('seconds_window', 3.0))

        if not access_token:
            return jsonify({'error': 'Missing access_token'}), 400

        if not prediction_csv_file_id:
            return jsonify({'error': 'Missing prediction_csv_file_id. Please select a prediction CSV file (output.csv).'}), 400

        creds = Credentials(token=access_token)
        drive_service = build('drive', 'v3', credentials=creds)

        # Get prediction CSV file info
        csv_metadata = drive_service.files().get(
            fileId=prediction_csv_file_id,
            fields='id,name,parents,webViewLink'
        ).execute()

        csv_name = csv_metadata.get('name', 'predictions.csv')
        if not csv_name.lower().endswith('.csv'):
            return jsonify({'error': 'Selected file is not a CSV file.'}), 400

        parents = csv_metadata.get('parents', [])
        if not parents:
            return jsonify({'error': 'Could not determine parent folder for CSV file.'}), 400

        video_folder_id = parents[0]
        video_metadata = drive_service.files().get(
            fileId=video_folder_id,
            fields='id,name'
        ).execute()
        video_folder_name = video_metadata.get('name', 'video')

        with tempfile.TemporaryDirectory() as temp_dir:
            # Download prediction CSV
            csv_path = os.path.join(temp_dir, csv_name)
            request_media = drive_service.files().get_media(fileId=prediction_csv_file_id)
            with open(csv_path, 'wb') as fh:
                fh.write(request_media.execute())

            # Generate review flags
            flags_csv_path, summary_csv_path, stats, flagged_frames = generate_review_flags(
                Path(csv_path),
                fps_video=fps_video,
                frame_stride=frame_stride,
                seconds_window=seconds_window,
            )

            # Upload flags CSV
            uploaded_flags = upload_file_to_drive(
                drive_service,
                str(flags_csv_path),
                video_folder_id,
                filename=os.path.basename(flags_csv_path),
                mime_type='text/csv',
            )

            # Upload summary CSV
            uploaded_summary = upload_file_to_drive(
                drive_service,
                str(summary_csv_path),
                video_folder_id,
                filename=os.path.basename(summary_csv_path),
                mime_type='text/csv',
            )

            # Copy flagged frames to watch folder
            requested, copied, watch_folder_id, watch_link = _copy_frames_to_watch(
                drive_service,
                video_folder_id,
                flagged_frames,
            )

        response_payload = {
            'video_folder_id': video_folder_id,
            'video_name': video_folder_name,
            'flag_csv_drive_id': uploaded_flags.get('id', ''),
            'flag_csv_drive_link': uploaded_flags.get('webViewLink', ''),
            'flag_summary_drive_id': uploaded_summary.get('id', ''),
            'flag_summary_drive_link': uploaded_summary.get('webViewLink', ''),
            'watch_folder_id': watch_folder_id,
            'watch_folder_link': watch_link or '',
            'watch_frames_requested': requested,
            'watch_frames_copied': copied,
            'review_stats': {
                'total_rows': stats.total_rows,
                'predicted_change_points': stats.predicted_change_points,
                'flagged_frames': stats.flagged_frames,
                'flagged_frames_pct': stats.flagged_frames_pct,
                'windows_count': stats.windows_count,
                'rows_covered_by_windows': stats.rows_covered_by_windows,
                'effective_fps': stats.effective_fps,
                'frame_stride': stats.frame_stride,
                'seconds_window': stats.seconds_window,
            },
        }

        return jsonify(response_payload)

    except Exception as err:
        import traceback
        return jsonify({'error': str(err), 'traceback': traceback.format_exc()}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

