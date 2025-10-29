#!/usr/bin/env python3
"""
Linux Mint Status Monitor
Monitors video processing status and sends updates to Mac backend
"""

import os
import json
import time
import requests
import glob
from pathlib import Path
from datetime import datetime

# Configuration
MAC_BACKEND_URL = "http://localhost:3001"  # This should be your Mac's IP
VIDEOS_DIR = "/home/morsestudio/sam2/videos"
RESULTS_DIR = "/home/morsestudio/sam2/results"
POLL_INTERVAL = 5  # seconds

def get_linux_status():
    """Get current status of Linux Mint processing"""
    status = {
        "timestamp": datetime.now().isoformat(),
        "videos_directory": VIDEOS_DIR,
        "results_directory": RESULTS_DIR,
        "videos": [],
        "results": [],
        "processing": [],
        "completed": []
    }
    
    # Check videos directory
    if os.path.exists(VIDEOS_DIR):
        video_files = glob.glob(f"{VIDEOS_DIR}/*.mp4") + glob.glob(f"{VIDEOS_DIR}/*.avi") + glob.glob(f"{VIDEOS_DIR}/*.mov")
        status["videos"] = [os.path.basename(f) for f in video_files]
    
    # Check results directory
    if os.path.exists(RESULTS_DIR):
        result_files = glob.glob(f"{RESULTS_DIR}/*")
        status["results"] = [os.path.basename(f) for f in result_files]
    
    # Check for processing indicators (lock files, temp files, etc.)
    processing_files = glob.glob(f"{VIDEOS_DIR}/*.processing") + glob.glob(f"{RESULTS_DIR}/*.processing")
    status["processing"] = [os.path.basename(f).replace('.processing', '') for f in processing_files]
    
    # Check for completed files
    completed_files = glob.glob(f"{RESULTS_DIR}/*_mouse_masks.npz")
    status["completed"] = [os.path.basename(f).replace('_mouse_masks.npz', '') for f in completed_files]
    
    return status

def send_status_to_mac(status):
    """Send status update to Mac backend"""
    try:
        response = requests.post(f"{MAC_BACKEND_URL}/api/linux-status-update", 
                               json=status, 
                               timeout=10)
        if response.status_code == 200:
            print(f"✅ Status sent to Mac: {len(status['videos'])} videos, {len(status['completed'])} completed")
        else:
            print(f"❌ Failed to send status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Could not connect to Mac backend: {e}")

def main():
    """Main monitoring loop"""
    print("🐧 Linux Mint Status Monitor Started")
    print(f"📁 Monitoring: {VIDEOS_DIR}")
    print(f"📊 Results: {RESULTS_DIR}")
    print(f"🔄 Polling every {POLL_INTERVAL} seconds")
    
    while True:
        try:
            status = get_linux_status()
            send_status_to_mac(status)
            
            # Print local status
            print(f"\n📊 Status Update - {datetime.now().strftime('%H:%M:%S')}")
            print(f"   Videos: {len(status['videos'])}")
            print(f"   Processing: {len(status['processing'])}")
            print(f"   Completed: {len(status['completed'])}")
            
            time.sleep(POLL_INTERVAL)
            
        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped by user")
            break
        except Exception as e:
            print(f"❌ Error in monitoring loop: {e}")
            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
