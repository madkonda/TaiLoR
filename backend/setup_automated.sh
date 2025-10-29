#!/bin/bash

# TaiLOR Linux Mint Setup Script (Fully Automated)
# This script sets up the Google Drive download functionality using service account

echo "🚀 Setting up TaiLOR Google Drive download on Linux Mint (Fully Automated)..."

# Create the videos directory
echo "📁 Creating videos directory..."
mkdir -p /home/morsestudio/sam2/videos
chmod 755 /home/morsestudio/sam2/videos

# Install required Python packages
echo "📦 Installing required Python packages..."
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Make the download script executable
echo "🔧 Making download script executable..."
chmod +x download_from_drive_automated.py

echo "✅ Setup complete!"
echo ""
echo "📋 How to use:"
echo "1. Make sure 'service-account-key.json' is in the same directory"
echo "2. Run: python download_from_drive_automated.py"
echo "3. Files will be downloaded automatically - no authorization needed!"
echo ""
echo "📁 Files will be downloaded to: /home/morsestudio/sam2/videos"
echo ""
echo "🔄 To run automatically every 5 minutes, add this to crontab:"
echo "   */5 * * * * cd /home/morsestudio/sam2/videologic && python download_from_drive_automated.py"
echo ""
echo "💡 This version uses service account authentication, so it's fully automated!"
