#!/bin/bash

echo "🚀 Setting up TaiLOR Google Drive Continuous Monitoring"
echo "======================================================"

# Configuration
SERVICE_NAME="tailor-drive-monitor"
SCRIPT_PATH="/home/morsestudio/sam2/monitor_drive_continuous.py"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

echo "📋 Configuration:"
echo "   Service Name: ${SERVICE_NAME}"
echo "   Script Path: ${SCRIPT_PATH}"
echo "   Service File: ${SERVICE_FILE}"

# 1. Copy the monitoring script to Linux Mint
echo "📄 Copying monitoring script..."
if [ -f "monitor_drive_continuous.py" ]; then
    cp monitor_drive_continuous.py "${SCRIPT_PATH}"
    chmod +x "${SCRIPT_PATH}"
    echo "✅ Monitoring script copied to ${SCRIPT_PATH}"
else
    echo "❌ Error: monitor_drive_continuous.py not found in current directory"
    exit 1
fi

# 2. Copy the service file
echo "🔧 Setting up systemd service..."
if [ -f "tailor-drive-monitor.service" ]; then
    sudo cp tailor-drive-monitor.service "${SERVICE_FILE}"
    echo "✅ Service file copied to ${SERVICE_FILE}"
else
    echo "❌ Error: tailor-drive-monitor.service not found in current directory"
    exit 1
fi

# 3. Reload systemd and enable service
echo "🔄 Configuring systemd service..."
sudo systemctl daemon-reload
sudo systemctl enable "${SERVICE_NAME}.service"
echo "✅ Service enabled"

# 4. Start the service
echo "🚀 Starting monitoring service..."
sudo systemctl start "${SERVICE_NAME}.service"
echo "✅ Service started"

# 5. Show status
echo "📊 Service status:"
sudo systemctl status "${SERVICE_NAME}.service" --no-pager

echo ""
echo "🎉 TaiLOR Google Drive Continuous Monitoring setup complete!"
echo ""
echo "📋 Useful commands:"
echo "   Check status: sudo systemctl status ${SERVICE_NAME}"
echo "   View logs: sudo journalctl -u ${SERVICE_NAME} -f"
echo "   Stop service: sudo systemctl stop ${SERVICE_NAME}"
echo "   Start service: sudo systemctl start ${SERVICE_NAME}"
echo "   Restart service: sudo systemctl restart ${SERVICE_NAME}"
echo ""
echo "🔧 The service will:"
echo "   - Monitor Google Drive folder every 30 seconds"
echo "   - Download new files automatically"
echo "   - Process video files with SAM2"
echo "   - Delete files from Google Drive after successful processing"
echo "   - Send real-time updates to Mac backend"


