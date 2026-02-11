# SAM2 Backend Service

Python backend service for processing video frames with SAM2 segmentation.

## Setup

### On GCP VM (where SAM2 is already installed)

1. **Copy files to VM** (from local machine; set `VM_ZONE`, `VM_PROJECT`, `VM_NAME`, `VM_USER` to your values):
```bash
gcloud compute scp --zone=YOUR_ZONE --project=YOUR_PROJECT_ID \
  backend/sam2_service.py \
  backend/api_server.py \
  backend/mouse_extraction.py \
  backend/rat_extraction.py \
  backend/rat2_extraction.py \
  backend/requirements.txt \
  VM_USER@VM_NAME:/home/VM_USER/sam2/backend/
```

2. **SSH into VM**:
```bash
gcloud compute ssh VM_NAME --zone=YOUR_ZONE --project=YOUR_PROJECT_ID
```

3. **Install dependencies**:
```bash
cd ~/sam2/backend
pip3 install -r requirements.txt
```

4. **Set environment variable** (optional, if SAM2 is not at ~/sam2):
```bash
export SAM2_BASE_DIR=~/sam2
```

5. **Verify SAM2 checkpoint exists**:
```bash
ls ~/sam2/checkpoints/sam2.1_hiera_large.pt
```

The service will automatically use:
- Checkpoint: `~/sam2/checkpoints/sam2.1_hiera_large.pt`
- Config: `~/sam2/configs/sam2.1/sam2.1_hiera_l.yaml`

If your SAM2 installation is in a different location, set `SAM2_BASE_DIR` environment variable.

## Running the API Server

**On the VM:**
```bash
cd ~/sam2/backend
python3 api_server.py
```

**Note:** The API server has CORS enabled for development. If you make changes to `api_server.py`, restart the server for changes to take effect:
```bash
# Stop the server (Ctrl+C), then restart:
python3 api_server.py
```

Or run in background with screen/tmux:
```bash
cd ~/sam2/backend
screen -S sam2-api
python3 api_server.py
# Press Ctrl+A then D to detach
```

**Note**: On Ubuntu/GCP VMs, use `python3` instead of `python`. They are equivalent and won't cause issues.

The server will run on `http://localhost:5000` by default (or the IP of your VM).

**Note**: Make sure the VM firewall allows incoming connections on port 5000 if accessing from outside.

To allow HTTP traffic:
```bash
gcloud compute firewall-rules create allow-sam2-api \
  --allow tcp:5000 \
  --source-ranges 0.0.0.0/0 \
  --description "Allow SAM2 API server" \
  --project=YOUR_PROJECT_ID
```

## API Endpoints

### POST /process-sam2

Process frames with SAM2 segmentation.

**Request body:**
```json
{
  "access_token": "Google OAuth access token",
  "frame_folder_id": "Google Drive folder ID",
  "video_folder_id": "Google Drive video folder (parent of frames)",
  "nest_point": {"x": 677, "y": 881},
  "mouse_point": {"x": 766, "y": 773},
  "ann_frame_idx": 0,
  "analysis_type": "mouse | rat | rat_only",
  "fixed_points_template": "mouse_less_nest",
  "nest_object_id": 1,
  "mouse_object_id": 2,
  "rat_object_id": 2,
  "rat_only_object_id": 1,
  "fixed_points": {
    "c1": {"x": 451, "y": 425},
    "c2": [1538, 384]
  }
}
```

**Response:**
```json
{
  "output_path": "/tmp/.../1.npz",
  "num_frames_processed": 180,
  "num_frames_total": 180,
  "npz_drive_id": "...",
  "npz_drive_link": "...",
  "csv_drive_id": "...",
  "csv_drive_link": "...",
  "prediction_drive_id": "...",
  "prediction_drive_link": "..."
}
```

### Fixed-Point Templates & Prediction

- `fixed_points_template` selects one of the bundled configurations (`mouse_less_nest`, `mouse_nest`, `rat1`, `rat2`, `rat3`, `rat4`, `rat5`).
- Each template loads its matching `fixed_points_configs/<name>.json`, applies the correct extractor, and runs the corresponding `*_tree_logic.py` model via `prediction.py`.
- The resulting prediction CSV is uploaded alongside the geometric features with the `<video>output.csv` naming scheme.

## GPU Support

The service automatically detects and uses:
- CUDA (NVIDIA GPUs) - Recommended
- MPS (Apple Silicon) - Preliminary support
- CPU - Fallback (very slow)

For best performance, use a CUDA-enabled GPU.

