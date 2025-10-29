#!/bin/bash

echo "🐧 Setting up Linux Mint Monitoring for TaiLOR"
echo "=============================================="

# Get Mac's IP address (you'll need to update this)
MAC_IP="192.168.1.100"  # Replace with your Mac's actual IP

echo "📋 Configuration:"
echo "   Mac Backend URL: http://$MAC_IP:3001"
echo "   Videos Directory: /home/morsestudio/sam2/videos"
echo "   Results Directory: /home/morsestudio/sam2/results"

# Create directories if they don't exist
echo "📁 Creating directories..."
mkdir -p /home/morsestudio/sam2/videos
mkdir -p /home/morsestudio/sam2/results

# Install Python requests if not already installed
echo "🐍 Installing Python dependencies..."
pip install requests

# Copy the monitoring script
echo "📄 Setting up monitoring script..."
cat > /home/morsestudio/sam2/linux_status.py << 'EOF'
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

# Configuration - UPDATE THIS WITH YOUR MAC'S IP
MAC_BACKEND_URL = "http://192.168.1.100:3001"  # UPDATE THIS!
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
EOF

# Make the script executable
chmod +x /home/morsestudio/sam2/linux_status.py

# Create a systemd service
echo "🔧 Creating systemd service..."
sudo tee /etc/systemd/system/tailor-linux-monitor.service > /dev/null << EOF
[Unit]
Description=TaiLOR Linux Mint Status Monitor
After=network.target

[Service]
Type=simple
User=morsestudio
WorkingDirectory=/home/morsestudio/sam2
ExecStart=/usr/bin/python3 /home/morsestudio/sam2/linux_status.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the service
echo "🚀 Starting monitoring service..."
sudo systemctl daemon-reload
sudo systemctl enable tailor-linux-monitor.service
sudo systemctl start tailor-linux-monitor.service

echo ""
echo "✅ Linux Mint monitoring setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Update the MAC_BACKEND_URL in /home/morsestudio/sam2/linux_status.py with your Mac's IP"
echo "2. Check service status: sudo systemctl status tailor-linux-monitor"
echo "3. View logs: sudo journalctl -u tailor-linux-monitor -f"
echo ""
echo "🔧 To update Mac IP address:"
echo "   sudo nano /home/morsestudio/sam2/linux_status.py"
echo "   # Change MAC_BACKEND_URL to your Mac's IP"
echo "   sudo systemctl restart tailor-linux-monitor"
