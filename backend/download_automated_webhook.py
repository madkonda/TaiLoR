#!/usr/bin/env python3
"""
TaiLOR Automated Google Drive Download Script with Webhook
Automatically downloads files when they're uploaded to Google Drive
"""

import os
import sys
import json
import time
import requests
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Configuration
DRIVE_FOLDER_ID = "1HvGlLB-MjcYftrQ-SHeopc913vSEUNKA"  # Your Google Drive folder ID
DOWNLOAD_DIR = "/home/morsestudio/sam2/videos"  # Local download directory
SERVICE_ACCOUNT_FILE = 'service-account-key.json'  # Service account key file
POLL_INTERVAL = 30  # Check for new files every 30 seconds
WEBHOOK_URL = "http://localhost:3001/api/download-complete"  # Webhook to notify Mac backend

def get_credentials():
    """Get service account credentials."""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        return credentials
    except FileNotFoundError:
        print(f"❌ Error: Service account file '{SERVICE_ACCOUNT_FILE}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading service account credentials: {e}")
        sys.exit(1)

def get_drive_files(service):
    """Get list of files from Google Drive folder."""
    try:
        results = service.files().list(
            q=f"'{DRIVE_FOLDER_ID}' in parents",
            fields="files(id, name, mimeType, modifiedTime)",
            orderBy="modifiedTime desc"
        ).execute()
        return results.get('files', [])
    except Exception as e:
        print(f"❌ Error listing files: {e}")
        return []

def download_file(service, file_id, file_name):
    """Download a single file from Google Drive."""
    try:
        print(f"📥 Downloading: {file_name}")
        
        # Download the file
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            if status:
                print(f"Download {int(status.progress() * 100)}%")
        
        # Save to local file
        file_path = Path(DOWNLOAD_DIR) / file_name
        with open(file_path, 'wb') as f:
            f.write(fh.getvalue())
        
        print(f"✅ Downloaded: {file_name}")
        return str(file_path)
        
    except Exception as e:
        print(f"❌ Error downloading {file_name}: {e}")
        return None

def notify_mac_backend(file_name, file_path):
    """Notify Mac backend that file has been downloaded."""
    try:
        payload = {
            "filename": file_name,
            "filepath": file_path,
            "status": "downloaded",
            "timestamp": time.time()
        }
        
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if response.status_code == 200:
            print(f"📡 Notified Mac backend: {file_name}")
        else:
            print(f"⚠️ Failed to notify Mac backend: {response.status_code}")
            
    except Exception as e:
        print(f"⚠️ Could not notify Mac backend: {e}")

def process_new_files(service, known_files):
    """Process new files that haven't been downloaded yet."""
    current_files = get_drive_files(service)
    new_files = []
    
    # Find files that are new or modified
    for file in current_files:
        file_id = file['id']
        if file_id not in known_files:
            new_files.append(file)
            known_files[file_id] = file
    
    # Download new files
    for file in new_files:
        file_id = file['id']
        file_name = file['name']
        
        # Skip if not a video file
        if not file_name.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.webm')):
            continue
            
        file_path = download_file(service, file_id, file_name)
        if file_path:
            notify_mac_backend(file_name, file_path)
    
    return known_files

def main():
    """Main automation loop."""
    print("🚀 TaiLOR Automated Google Drive Download Service")
    print(f"📁 Monitoring folder: {DRIVE_FOLDER_ID}")
    print(f"💾 Downloading to: {DOWNLOAD_DIR}")
    print(f"⏱️ Polling every {POLL_INTERVAL} seconds")
    print("=" * 60)
    
    # Create download directory
    download_path = Path(DOWNLOAD_DIR)
    download_path.mkdir(parents=True, exist_ok=True)
    
    # Get credentials
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    # Get initial file list
    known_files = {}
    initial_files = get_drive_files(service)
    for file in initial_files:
        known_files[file['id']] = file
    
    print(f"📋 Found {len(known_files)} existing files")
    print("🔄 Starting monitoring loop...")
    print()
    
    try:
        while True:
            known_files = process_new_files(service, known_files)
            time.sleep(POLL_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")
    except Exception as e:
        print(f"\n❌ Error in monitoring loop: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
