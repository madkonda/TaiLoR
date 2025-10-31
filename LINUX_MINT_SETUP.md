# Linux Mint Setup - Rclone Based

## Overview

Linux Mint uses **rclone** to mount Google Drive and watch for new video files. This is simpler than API downloads.

## Required Files to Copy:

1. **`backend/monitor_drive_rclone.py`**
   - Location on Linux Mint: `/home/morsestudio/sam2/logic/monitor_drive_rclone.py`
   - Purpose: Watches mounted Google Drive folder for new videos

2. **`backend/tailor-rclone-monitor.service`**
   - Location on Linux Mint: `/etc/systemd/system/tailor-rclone-monitor.service`
   - Purpose: Run monitor as a system service

**Note**: No service account key needed! rclone uses OAuth (already configured)

### Required Directories:

```bash
sudo mkdir -p /home/morsestudio/sam2/videos
sudo mkdir -p /home/morsestudio/sam2/results
sudo chown -R morsestudio:morsestudio /home/morsestudio/sam2
```

### Required Python Script (if not already there):

- **`/home/morsestudio/sam2/videologic/process_video_linux.py`**
  - Your SAM2 video processing script (should already exist)

### Installation Steps on Linux Mint:

1. **Copy files:**
   ```bash
   # SSH to Linux Mint or use SCP
   scp backend/monitor_drive_continuous.py morsestudio@MINT_PC_IP:/home/morsestudio/sam2/
   scp backend/service-account-key.json morsestudio@MINT_PC_IP:/home/morsestudio/sam2/
   ```

2. **Install Python dependencies:**
   ```bash
   pip3 install google-api-python-client google-auth requests
   # OR if using conda environment:
   /home/morsestudio/anaconda3/envs/sam2/bin/pip install google-api-python-client google-auth requests
   ```

3. **Set up systemd service (optional):**
   ```bash
   sudo cp backend/tailor-drive-monitor.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable tailor-drive-monitor
   sudo systemctl start tailor-drive-monitor
   ```

4. **Verify monitor script works:**
   ```bash
   cd /home/morsestudio/sam2
   python3 monitor_drive_continuous.py
   ```

## What Does NOT Go to Linux Mint

- ❌ `backend/server.js` - This is the API server, should run elsewhere
- ❌ `backend/package.json` - Not needed on Linux Mint
- ❌ Frontend files - These are on Vercel
- ❌ Node.js backend - Only Python monitor script needed

## Backend Server Location

The backend API (`server.js`) should run on:
- Your Mac (for testing) - currently running on `localhost:3001`
- OR a server accessible at `api.mintpc.morsestudio.dev`
- **NOT on Linux Mint** - Linux Mint is only for video processing

## Summary

**Linux Mint needs:**
- ✅ `monitor_drive_continuous.py` 
- ✅ `service-account-key.json`
- ✅ Python dependencies (google-api-python-client, etc.)
- ✅ SAM2 processing script (process_video_linux.py)
- ✅ Directories for videos and results

**Linux Mint does NOT need:**
- ❌ Node.js backend server
- ❌ Backend API (`server.js`)
- ❌ Frontend files

