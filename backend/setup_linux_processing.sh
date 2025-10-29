#!/bin/bash

# TaiLOR Linux Mint Video Processing Setup Script
# This script transfers the processing script to Linux Mint and sets it up

echo "🚀 Setting up video processing on Linux Mint..."

# Configuration
LINUX_MINT_USER="morsestudio"
LINUX_MINT_HOST="mintpc.morsestudio.dev"
LINUX_MINT_PATH="/home/morsestudio/sam2/videologic"

# Files to transfer
FILES_TO_TRANSFER=(
    "process_video_linux.py"
    "download_from_drive_automated.py"
)

echo "📤 Transferring files to Linux Mint..."

# Transfer each file
for file in "${FILES_TO_TRANSFER[@]}"; do
    if [ -f "$file" ]; then
        echo "📁 Transferring $file..."
        scp -o "ProxyCommand cloudflared access ssh --hostname $LINUX_MINT_HOST" \
            "$file" \
            "$LINUX_MINT_USER@$LINUX_MINT_HOST:$LINUX_MINT_PATH/"
        
        if [ $? -eq 0 ]; then
            echo "✅ Successfully transferred $file"
        else
            echo "❌ Failed to transfer $file"
            exit 1
        fi
    else
        echo "⚠️ File not found: $file"
    fi
done

echo "🔧 Setting up permissions on Linux Mint..."

# Set up permissions and make scripts executable
ssh -o "ProxyCommand cloudflared access ssh --hostname $LINUX_MINT_HOST" \
    "$LINUX_MINT_USER@$LINUX_MINT_HOST" << 'EOF'
    cd /home/morsestudio/sam2/videologic
    
    # Make scripts executable
    chmod +x process_video_linux.py
    chmod +x download_from_drive_automated.py
    
    # Create results directory
    mkdir -p /home/morsestudio/sam2/results
    
    echo "✅ Permissions set and directories created"
EOF

if [ $? -eq 0 ]; then
    echo "✅ Linux Mint setup completed successfully!"
    echo ""
    echo "📋 Next steps:"
    echo "1. Restart the download service on Linux Mint:"
    echo "   sudo systemctl restart tailor-download.service"
    echo ""
    echo "2. Check service status:"
    echo "   sudo systemctl status tailor-download.service"
    echo ""
    echo "3. Monitor logs:"
    echo "   sudo journalctl -u tailor-download.service -f"
    echo ""
    echo "🎉 Video processing is now fully automated on Linux Mint!"
else
    echo "❌ Failed to set up Linux Mint"
    exit 1
fi
