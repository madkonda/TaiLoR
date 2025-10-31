#!/bin/bash
# Setup script for rclone on Linux Mint

echo "🔧 Setting up rclone for TaiLOR on Linux Mint"
echo ""

# Check if rclone is installed
if ! command -v rclone &> /dev/null; then
    echo "📦 Installing rclone..."
    curl https://rclone.org/install.sh | sudo bash
else
    echo "✅ rclone is already installed"
fi

# Create mount point
MOUNT_POINT="/mnt/googledrive"
echo "📁 Creating mount point: $MOUNT_POINT"
sudo mkdir -p $MOUNT_POINT
sudo chown morsestudio:morsestudio $MOUNT_POINT
sudo chmod 755 $MOUNT_POINT

# Configure rclone (interactive)
echo ""
echo "🔐 Setting up Google Drive connection..."
echo "You'll need to:"
echo "1. Go to https://console.cloud.google.com/apis/credentials"
echo "2. Create OAuth 2.0 credentials"
echo "3. Download client_id and client_secret"
echo ""
read -p "Press Enter when ready to configure rclone..."

rclone config

# Create directories in Drive
echo "📁 Creating directories in Google Drive..."
rclone mkdir gdrive:TaiLOR/videos
rclone mkdir gdrive:TaiLOR/results

# Test mount
echo "🧪 Testing mount..."
rclone mount gdrive: $MOUNT_POINT --daemon --vfs-cache-mode writes

sleep 3

if mountpoint -q $MOUNT_POINT; then
    echo "✅ Mount successful!"
    echo ""
    echo "📋 To make mount permanent, add to /etc/fstab or use systemd:"
    echo ""
    echo "Create /etc/systemd/system/rclone-mount.service:"
    echo "[Unit]"
    echo "Description=rclone Google Drive mount"
    echo "After=network-online.target"
    echo ""
    echo "[Service]"
    echo "Type=notify"
    echo "User=morsestudio"
    echo "ExecStart=/usr/bin/rclone mount gdrive: $MOUNT_POINT --vfs-cache-mode writes"
    echo "Restart=always"
    echo "RestartSec=10"
    echo ""
    echo "[Install]"
    echo "WantedBy=multi-user.target"
else
    echo "❌ Mount failed. Check rclone configuration."
    exit 1
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Install Python watchdog: pip3 install watchdog"
echo "2. Copy monitor_drive_rclone.py to /home/morsestudio/sam2/logic/"
echo "3. Update paths in monitor_drive_rclone.py if needed"
echo "4. Run: python3 /home/morsestudio/sam2/logic/monitor_drive_rclone.py"

