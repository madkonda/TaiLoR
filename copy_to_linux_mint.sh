#!/bin/bash
# Script to copy required files to Linux Mint PC

# Configuration - UPDATE THESE
MINT_PC_IP="192.168.1.100"  # Change to your Linux Mint PC IP
MINT_USER="morsestudio"
MINT_SAM2_DIR="/home/morsestudio/sam2"

echo "📋 Copying TaiLOR files to Linux Mint PC..."
echo "Target: ${MINT_USER}@${MINT_PC_IP}:${MINT_SAM2_DIR}"
echo ""

# Copy monitor script
echo "📄 Copying monitor_drive_continuous.py..."
scp backend/monitor_drive_continuous.py ${MINT_USER}@${MINT_PC_IP}:${MINT_SAM2_DIR}/

# Copy service account key (if exists)
if [ -f "backend/service-account-key.json" ]; then
    echo "🔑 Copying service-account-key.json..."
    scp backend/service-account-key.json ${MINT_USER}@${MINT_PC_IP}:${MINT_SAM2_DIR}/
else
    echo "⚠️  service-account-key.json not found! You need to copy it manually."
fi

# Copy systemd service file
echo "⚙️  Copying systemd service file..."
scp backend/tailor-drive-monitor.service ${MINT_USER}@${MINT_PC_IP}:/tmp/

echo ""
echo "✅ Files copied!"
echo ""
echo "Next steps on Linux Mint PC:"
echo "1. Move service file: sudo mv /tmp/tailor-drive-monitor.service /etc/systemd/system/"
echo "2. Install Python deps: pip3 install google-api-python-client google-auth requests"
echo "3. Create directories: mkdir -p /home/morsestudio/sam2/videos /home/morsestudio/sam2/results"
echo "4. Enable service: sudo systemctl daemon-reload && sudo systemctl enable --now tailor-drive-monitor"

