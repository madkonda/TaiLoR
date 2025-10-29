#!/bin/bash

# TaiLOR Monitoring Setup Script
# Sets up automated Google Drive monitoring

echo "🚀 Setting up TaiLOR Google Drive Monitoring"

# Stop the failing service
sudo systemctl stop tailor-download.service

# Install the corrected service file
sudo cp tailor-download.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Start the service
sudo systemctl start tailor-download.service

# Enable auto-start
sudo systemctl enable tailor-download.service

echo "✅ Service setup complete!"
echo ""
echo "📊 Service status:"
sudo systemctl status tailor-download.service --no-pager

echo ""
echo "📋 Useful commands:"
echo "  Check status: sudo systemctl status tailor-download.service"
echo "  View logs:    sudo journalctl -u tailor-download.service -f"
echo "  Restart:      sudo systemctl restart tailor-download.service"
echo ""
echo "🎯 The service will now monitor Google Drive every 30 seconds"
echo "   and automatically download new files to ~/sam2/videos"
