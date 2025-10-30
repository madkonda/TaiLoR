#!/usr/bin/env python3
"""
Linux Mint File Server
Simple FastAPI server to serve file listings and processing
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import glob
from pathlib import Path
from datetime import datetime
import subprocess
import json

app = FastAPI(title="Linux Mint File Server", version="1.0.0")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
VIDEOS_DIR = "/home/morsestudio/sam2/videos"
RESULTS_DIR = "/home/morsestudio/sam2/results"
SAM2_SCRIPT = "/home/morsestudio/sam2/videologic/process_video_linux.py"

@app.get("/")
async def root():
    return {"message": "Linux Mint File Server is running", "status": "ok"}

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/list-files")
async def list_files():
    """List all files in videos and results directories"""
    try:
        files = {
            "videos": [],
            "results": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # List video files
        if os.path.exists(VIDEOS_DIR):
            video_files = glob.glob(f"{VIDEOS_DIR}/*.mp4") + glob.glob(f"{VIDEOS_DIR}/*.avi") + glob.glob(f"{VIDEOS_DIR}/*.mov") + glob.glob(f"{VIDEOS_DIR}/*.webm") + glob.glob(f"{VIDEOS_DIR}/*.mkv")
            for f in video_files:
                file_info = {
                    "name": os.path.basename(f),
                    "path": f,
                    "size": os.path.getsize(f),
                    "modified": datetime.fromtimestamp(os.path.getmtime(f)).isoformat(),
                    "type": "video"
                }
                files["videos"].append(file_info)
        
        # List result directories
        if os.path.exists(RESULTS_DIR):
            result_dirs = [d for d in os.listdir(RESULTS_DIR) if os.path.isdir(os.path.join(RESULTS_DIR, d))]
            for d in result_dirs:
                dir_path = os.path.join(RESULTS_DIR, d)
                file_info = {
                    "name": d,
                    "path": dir_path,
                    "size": sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))),
                    "modified": datetime.fromtimestamp(os.path.getmtime(dir_path)).isoformat(),
                    "type": "directory"
                }
                files["results"].append(file_info)
        
        return files
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/process-video")
async def process_video(data: dict):
    """Process a video with SAM2 segmentation"""
    try:
        video_path = data.get("video_path")
        nest_x = data.get("nest_x", 677)
        nest_y = data.get("nest_y", 881)
        mouse_x = data.get("mouse_x", 766)
        mouse_y = data.get("mouse_y", 773)
        
        if not video_path or not os.path.exists(video_path):
            raise HTTPException(status_code=400, detail="Video file not found")
        
        # Run SAM2 processing
        cmd = [
            'python3',
            SAM2_SCRIPT,
            '--video_path', video_path,
            '--nest_x', str(nest_x),
            '--nest_y', str(nest_y),
            '--mouse_x', str(mouse_x),
            '--mouse_y', str(mouse_y),
            '--output_dir', RESULTS_DIR
        ]
        
        # Start processing in background
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        return {
            "success": True,
            "message": "Processing started",
            "video_path": video_path,
            "coordinates": {"nest": [nest_x, nest_y], "mouse": [mouse_x, mouse_y]},
            "process_id": process.pid
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/process-status/{process_id}")
async def process_status(process_id: int):
    """Check processing status"""
    try:
        # Simple status check - in production you'd track this properly
        return {
            "process_id": process_id,
            "status": "running",  # or "completed", "failed"
            "message": "Processing in progress"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Linux Mint File Server...")
    print(f"📁 Videos Directory: {VIDEOS_DIR}")
    print(f"📊 Results Directory: {RESULTS_DIR}")
    print(f"🔬 SAM2 Script: {SAM2_SCRIPT}")
    uvicorn.run(app, host="0.0.0.0", port=8080)


