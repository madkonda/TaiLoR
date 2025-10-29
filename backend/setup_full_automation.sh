#!/bin/bash

# TaiLOR Full Automation Setup Script
# Sets up complete automated workflow: Frontend → Drive → Linux Mint

echo "🚀 Setting up TaiLOR Full Automation System"
echo "============================================="

# Create the videos directory
echo "📁 Creating videos directory..."
mkdir -p /home/morsestudio/sam2/videos
chmod 755 /home/morsestudio/sam2/videos

# Install required Python packages
echo "📦 Installing required Python packages..."
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests

# Make scripts executable
echo "🔧 Making scripts executable..."
chmod +x download_automated_webhook.py
chmod +x download_from_drive_automated.py

# Install systemd service
echo "⚙️ Installing systemd service..."
sudo cp tailor-download.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable tailor-download.service

echo "✅ Setup complete!"
echo ""
echo "🎯 Full Automation Workflow:"
echo "1. User uploads video on frontend (https://tailor.morsestudio.dev)"
echo "2. Mac backend uploads to Google Drive automatically"
echo "3. Linux Mint monitors Google Drive and downloads new files"
echo "4. Linux Mint notifies Mac backend when download is complete"
echo "5. You can add SAM2 processing here!"
echo ""
echo "🚀 Starting the download service..."
sudo systemctl start tailor-download.service

echo "📊 Service status:"
sudo systemctl status tailor-download.service --no-pager

echo ""
echo "📋 Useful commands:"
echo "  Check status: sudo systemctl status tailor-download.service"
echo "  View logs:    sudo journalctl -u tailor-download.service -f"
echo "  Stop service: sudo systemctl stop tailor-download.service"
echo "  Start service: sudo systemctl start tailor-download.service"
echo ""
echo "🎉 Full automation is now active!"
