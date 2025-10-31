#!/usr/bin/env python3
# Install dependencies: pip3 install watchdog requests
"""
TaiLOR Google Drive Monitor using rclone (Folder Watcher)
Monitors a mounted Google Drive folder for new video files and processes them automatically
Uses rclone mount instead of API downloads - much simpler!
"""

import os
import sys
import time
import requests
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
RCLONE_MOUNT_POINT = "/mnt/googledrive"  # Where rclone mounts Google Drive
DRIVE_VIDEOS_DIR = "/mnt/googledrive/TaiLOR/videos"  # Watch this folder
DRIVE_RESULTS_DIR = "/mnt/googledrive/TaiLOR/results"  # Save results here
LOCAL_RESULTS_DIR = "/home/morsestudio/sam2/results"  # Also save locally
WEBHOOK_URL = "https://api.mintpc.morsestudio.dev/api/processing-complete"

# Track processed files to avoid reprocessing
processed_files = set()

class VideoFileHandler(FileSystemEventHandler):
    """Handle new video files appearing in the watched folder"""
    
    def on_created(self, event):
        """Called when a new file is created"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Only process video files
        if not file_path.suffix.lower() in ['.mp4', '.avi', '.mov', '.mkv', '.webm']:
            return
        
        # Check if already processed
        file_id = str(file_path)
        if file_id in processed_files:
            return
        
        # Wait for file to finish syncing (Google Drive Desktop/rclone might still be writing)
        print(f"⏳ Waiting for {file_path.name} to finish syncing...")
        time.sleep(5)
        
        # Check if file is complete (no longer changing)
        old_size = 0
        for _ in range(10):  # Check for 10 seconds
            try:
                current_size = file_path.stat().st_size
                if current_size == old_size and current_size > 0:
                    break
                old_size = current_size
                time.sleep(1)
            except:
                pass
        
        print(f"🎬 New video detected: {file_path.name}")
        print(f"📁 Full path: {file_path}")
        
        # Process the video
        process_video(file_path)
        processed_files.add(file_id)

def process_video(video_path):
    """Process a video file with default coordinates"""
    try:
        video_name = video_path.name
        video_basename = Path(video_name).stem  # e.g., "1" from "1.mp4"
        print(f"🔬 Starting processing for {video_name}")
        
        # Extract job ID from filename if available (format: jobId_filename.mp4)
        job_id = None
        if '_' in video_name:
            potential_job_id = video_name.split('_')[0]
            if potential_job_id.startswith('job_'):
                job_id = potential_job_id
        
        # Create organized output directories for this video
        video_output_dir = Path(LOCAL_RESULTS_DIR) / video_basename
        video_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for organization
        (video_output_dir / "frames").mkdir(exist_ok=True)
        (video_output_dir / "segmentation").mkdir(exist_ok=True)
        
        # Default coordinates
        nest_coords = [677, 881]
        mouse_coords = [766, 773]
        
        print(f"🎯 Using coordinates - Nest: {nest_coords}, Mouse: {mouse_coords}")
        print(f"📁 Output directory: {video_output_dir}")
        
        # Send processing start notification
        send_notification(video_name, str(video_path), "processing", "extract", job_id)
        
        # Run SAM2 processing - save to organized folder
        cmd = [
            'python3',
            '/home/morsestudio/sam2/videologic/process_video_linux.py',
            '--video_path', str(video_path),
            '--nest_x', str(nest_coords[0]),
            '--nest_y', str(nest_coords[1]),
            '--mouse_x', str(mouse_coords[0]),
            '--mouse_y', str(mouse_coords[1]),
            '--output_dir', str(video_output_dir)
        ]
        
        send_notification(video_name, str(video_path), "processing", "segment", job_id)
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Processing completed for {video_name}")
        
        # Copy results to Drive folder in organized structure
        copy_results_to_drive(video_name, video_basename, video_output_dir)
        
        # Send completion notification
        send_notification(video_name, str(video_path), "completed", "complete", job_id)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Processing failed for {video_name}: {e}")
        print(f"Error output: {e.stderr}")
        send_notification(video_name, str(video_path), "failed", "segment", job_id)
        return False
    except Exception as e:
        print(f"❌ Error processing {video_name}: {e}")
        send_notification(video_name, str(video_path), "failed", "segment", job_id)
        return False

def copy_results_to_drive(video_name, video_basename, video_output_dir):
    """Copy processing results to Google Drive in organized folder structure"""
    try:
        import shutil
        
        # Create organized folder in Drive: results/{video_basename}/
        drive_video_results_dir = Path(DRIVE_RESULTS_DIR) / video_basename
        drive_video_results_dir.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories in Drive
        (drive_video_results_dir / "frames").mkdir(exist_ok=True)
        (drive_video_results_dir / "segmentation").mkdir(exist_ok=True)
        
        # Copy all files from local output directory to Drive
        if not video_output_dir.exists():
            print(f"⚠️ No results directory found: {video_output_dir}")
            return
        
        # Find all result files recursively
        result_files = []
        for ext in ['*.npz', '*.npy', '*.json', '*.png', '*.jpg', '*.txt', '*.csv']:
            result_files.extend(video_output_dir.rglob(ext))
        
        if not result_files:
            # Also try to copy entire directory structure
            print(f"📂 Copying entire directory structure to Drive...")
            if video_output_dir.is_dir():
                # Copy directory structure recursively
                for item in video_output_dir.rglob('*'):
                    if item.is_file():
                        # Maintain relative path structure
                        relative_path = item.relative_to(video_output_dir)
                        dest = drive_video_results_dir / relative_path
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(item, dest)
                        print(f"📤 Copied: {relative_path}")
        else:
            # Copy individual files maintaining structure
            for result_file in result_files:
                relative_path = result_file.relative_to(video_output_dir)
                dest = drive_video_results_dir / relative_path
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(result_file, dest)
                print(f"📤 Copied to Drive: {relative_path}")
        
        print(f"✅ Results copied to Google Drive: {drive_video_results_dir}")
        
    except Exception as e:
        print(f"⚠️ Error copying results to Drive: {e}")

def send_notification(filename, filepath, status, step=None, job_id=None):
    """Send processing notification to backend"""
    try:
        payload = {
            "filename": filename,
            "filepath": filepath,
            "status": status,
            "timestamp": int(time.time()),
            "type": "video_processing",
            "step": step,
            "jobId": job_id
        }
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        response.raise_for_status()
        print(f"🔔 Notification sent: {filename} - {status} ({step})")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Warning: Could not send notification: {e}")

def check_rclone_mount():
    """Verify rclone mount is active"""
    if not os.path.exists(RCLONE_MOUNT_POINT):
        print(f"❌ Error: Rclone mount point not found: {RCLONE_MOUNT_POINT}")
        print("📋 Please mount Google Drive first:")
        print(f"   rclone mount gdrive: {RCLONE_MOUNT_POINT} --daemon")
        sys.exit(1)
    
    if not os.path.ismount(RCLONE_MOUNT_POINT):
        print(f"⚠️ Warning: {RCLONE_MOUNT_POINT} exists but is not mounted")
        print("📋 Please mount Google Drive:")
        print(f"   rclone mount gdrive: {RCLONE_MOUNT_POINT} --daemon")
        sys.exit(1)
    
    print(f"✅ Rclone mount verified: {RCLONE_MOUNT_POINT}")

def main():
    """Main monitoring loop"""
    print("🚀 Starting TaiLOR Google Drive Monitor (rclone-based)")
    print(f"📁 Watching: {DRIVE_VIDEOS_DIR}")
    print(f"📊 Results: {DRIVE_RESULTS_DIR}")
    print()
    
    # Check rclone mount
    check_rclone_mount()
    
    # Ensure directories exist
    Path(DRIVE_VIDEOS_DIR).mkdir(parents=True, exist_ok=True)
    Path(DRIVE_RESULTS_DIR).mkdir(parents=True, exist_ok=True)
    Path(LOCAL_RESULTS_DIR).mkdir(parents=True, exist_ok=True)
    
    # Set up file watcher
    event_handler = VideoFileHandler()
    observer = Observer()
    observer.schedule(event_handler, DRIVE_VIDEOS_DIR, recursive=False)
    observer.start()
    
    print(f"👀 Watching for new videos in {DRIVE_VIDEOS_DIR}...")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping monitor...")
        observer.stop()
    
    observer.join()
    print("✅ Monitor stopped")

if __name__ == "__main__":
    main()

