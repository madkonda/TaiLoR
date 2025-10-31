# Rclone Setup Guide for Linux Mint

## Overview

Instead of using Google Drive API to download files, we'll use `rclone` to mount Google Drive as a local folder. This is much simpler!

## Architecture

```
Backend (Mac) → Google Drive API → Upload to Drive
                                      ↓
Linux Mint: rclone mount → Access Drive as local folder → Watch for new files → Process
```

## Benefits

- ✅ No API download code needed
- ✅ Simpler file monitoring (just watch a folder)
- ✅ Automatic file detection
- ✅ No service account credentials needed
- ✅ No API rate limits

## Setup Steps

### 1. Install rclone on Linux Mint

```bash
curl https://rclone.org/install.sh | sudo bash
```

### 2. Configure rclone with Google Drive

```bash
rclone config
```

Follow the prompts:
- Name: `gdrive` (or any name you prefer)
- Storage: `drive` (Google Drive)
- Client ID: (optional, can leave blank for default)
- Client Secret: (optional)
- Scope: `drive` (full access)
- Service Account: (leave blank)
- Auth: Choose browser authentication

This will:
1. Open a browser for Google authentication
2. Give rclone access to your Google Drive
3. Save credentials automatically

### 3. Create Mount Point

```bash
sudo mkdir -p /mnt/googledrive
sudo chown morsestudio:morsestudio /mnt/googledrive
sudo chmod 755 /mnt/googledrive
```

### 4. Create Directories in Google Drive

```bash
rclone mkdir gdrive:TaiLOR/videos
rclone mkdir gdrive:TaiLOR/results
```

### 5. Test Mount

```bash
rclone mount gdrive: /mnt/googledrive --daemon --vfs-cache-mode writes
```

Verify:
```bash
ls /mnt/googledrive/TaiLOR/videos
```

### 6. Make Mount Permanent (systemd)

Create `/etc/systemd/system/rclone-mount.service`:

```ini
[Unit]
Description=rclone Google Drive mount
After=network-online.target

[Service]
Type=notify
User=morsestudio
ExecStart=/usr/bin/rclone mount gdrive: /mnt/googledrive --vfs-cache-mode writes
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable rclone-mount
sudo systemctl start rclone-mount
```

### 7. Install Python Dependencies

```bash
pip3 install watchdog requests
# OR if using conda:
/home/morsestudio/anaconda3/envs/sam2/bin/pip install watchdog requests
```

### 8. Copy Monitor Script

```bash
scp backend/monitor_drive_rclone.py morsestudio@MINT_PC:/home/morsestudio/sam2/logic/
scp backend/tailor-rclone-monitor.service morsestudio@MINT_PC:/tmp/
```

### 9. Setup systemd Service

```bash
sudo cp /tmp/tailor-rclone-monitor.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable tailor-rclone-monitor
sudo systemctl start tailor-rclone-monitor
```

### 10. Verify It Works

```bash
# Check mount
mountpoint /mnt/googledrive

# Check service
sudo systemctl status tailor-rclone-monitor

# Watch logs
sudo journalctl -u tailor-rclone-monitor -f
```

## File Structure

After setup:
```
/mnt/googledrive/
└── TaiLOR/
    ├── videos/    ← Backend uploads here, Linux Mint watches this
    └── results/   ← Linux Mint saves results here, auto-syncs back
```

## How It Works

1. **Backend** uploads video to Google Drive via API
2. **Google Drive** syncs to cloud
3. **rclone mount** makes Drive accessible as `/mnt/googledrive/`
4. **Monitor script** watches `/mnt/googledrive/TaiLOR/videos/` for new files
5. When new file appears → **Process video** with SAM2
6. **Save results** to both:
   - Local: `/home/morsestudio/sam2/results/`
   - Drive: `/mnt/googledrive/TaiLOR/results/` (auto-syncs back to Mac)

## Troubleshooting

**Mount not working?**
```bash
# Check if rclone is running
ps aux | grep rclone

# Check mount point
mountpoint /mnt/googledrive

# Remount
sudo umount /mnt/googledrive
rclone mount gdrive: /mnt/googledrive --daemon --vfs-cache-mode writes
```

**Files not appearing?**
- Check rclone mount is active: `mountpoint /mnt/googledrive`
- Verify files exist in Drive: `rclone ls gdrive:TaiLOR/videos`
- Check rclone logs: `journalctl -u rclone-mount -f`

**Monitor not detecting files?**
- Check service is running: `sudo systemctl status tailor-rclone-monitor`
- Check logs: `sudo journalctl -u tailor-rclone-monitor -f`
- Verify directory permissions

## Next Steps

1. Backend continues using Google Drive API (no changes needed) ✅
2. Linux Mint uses rclone mount (new simpler approach) ✅
3. Upload a test video and watch it process automatically! 🎬

