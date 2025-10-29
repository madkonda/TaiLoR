#!/bin/bash

# TaiLOR Linux Mint Setup Script
# This script sets up the Google Drive download functionality

echo "🚀 Setting up TaiLOR Google Drive download on Linux Mint..."

# Create the videos directory
echo "📁 Creating videos directory..."
mkdir -p /home/morsestudio/sam2/videos
chmod 755 /home/morsestudio/sam2/videos

# Install required Python packages
echo "📦 Installing required Python packages..."
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Make the download script executable
echo "🔧 Making download script executable..."
chmod +x download_from_drive.py

echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Download your OAuth2 credentials from Google Cloud Console"
echo "2. Save them as 'credentials.json' in this directory"
echo "3. Run: python download_from_drive.py"
echo ""
echo "📁 Files will be downloaded to: /home/morsestudio/sam2/videos"
