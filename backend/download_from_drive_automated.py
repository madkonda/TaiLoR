#!/usr/bin/env python3
"""
TaiLOR Google Drive Download Script for Linux Mint (Fully Automated)
Downloads files from Google Drive folder to local directory using service account
Automatically deletes files from Google Drive after successful processing
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

# Google Drive API scopes - now includes delete permission
SCOPES = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/drive.file']

# Configuration
DRIVE_FOLDER_ID = "1HvGlLB-MjcYftrQ-SHeopc913vSEUNKA"  # Your Google Drive folder ID
DOWNLOAD_DIR = "/home/morsestudio/sam2/videos"  # Local download directory
SERVICE_ACCOUNT_FILE = 'service-account-key.json'  # Service account key file
WEBHOOK_URL = "http://192.168.1.100:3001/api/download-complete"  # Mac backend webhook URL

def get_credentials():
    """Get service account credentials."""
    try:
        # Load service account credentials
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        return credentials
    except FileNotFoundError:
        print(f"❌ Error: Service account file '{SERVICE_ACCOUNT_FILE}' not found!")
        print("📋 Please make sure you have the service account key file.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading service account credentials: {e}")
        sys.exit(1)

def delete_file_from_drive(service, file_id, file_name):
    """Delete a file from Google Drive."""
    try:
        service.files().delete(fileId=file_id).execute()
        print(f"🗑️ Deleted from Google Drive: {file_name}")
        return True
    except Exception as e:
        print(f"❌ Error deleting {file_name} from Google Drive: {e}")
        return False

def download_files_from_drive():
    """Download all files from the specified Google Drive folder."""
    try:
        # Get credentials
        creds = get_credentials()
        service = build('drive', 'v3', credentials=creds)
        
        # Create download directory
        download_path = Path(DOWNLOAD_DIR)
        download_path.mkdir(parents=True, exist_ok=True)
        
        # List files in the folder
        results = service.files().list(
            q=f"'{DRIVE_FOLDER_ID}' in parents",
            fields="files(id, name, mimeType)"
        ).execute()
        
        files = results.get('files', [])
        
        if not files:
            print("No files found in the Google Drive folder.")
            return
        
        print(f"Found {len(files)} files in Google Drive folder:")
        
        for file in files:
            file_id = file['id']
            file_name = file['name']
            file_path = download_path / file_name
            
            print(f"Downloading: {file_name}")
            
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
            with open(file_path, 'wb') as f:
                f.write(fh.getvalue())
            
            print(f"✅ Downloaded: {file_name}")
            
            # Auto-process video files
            if file_name.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.webm')):
                print(f"🎬 Auto-processing video: {file_name}")
                # Extract job ID from filename if available (format: jobId_filename.mp4)
                job_id = None
                if '_' in file_name:
                    potential_job_id = file_name.split('_')[0]
                    if potential_job_id.startswith('job_'):
                        job_id = potential_job_id
                
                # Process the video and delete from Google Drive if successful
                success = process_video_automatically(file_path, file_name, job_id, service, file_id)
                
                # Delete from Google Drive after successful processing
                if success:
                    delete_file_from_drive(service, file_id, file_name)
                else:
                    print(f"⚠️ Keeping {file_name} in Google Drive due to processing failure")
            else:
                # For non-video files, delete immediately after download
                print(f"📄 Non-video file downloaded, deleting from Google Drive: {file_name}")
                delete_file_from_drive(service, file_id, file_name)
        
        print(f"\n🎉 All files downloaded to: {DOWNLOAD_DIR}")
        
    except Exception as e:
        print(f"❌ Error downloading files: {e}")
        sys.exit(1)

def process_video_automatically(video_path, video_name, job_id=None, service=None, file_id=None):
    """
    Automatically process a downloaded video with default coordinates
    Returns True if successful, False otherwise
    """
    try:
        import subprocess
        
        # Default coordinates (can be customized)
        nest_coords = [677, 881]  # Default nest position
        mouse_coords = [766, 773]  # Default mouse position
        
        print(f"🔬 Starting automatic processing for {video_name}")
        print(f"🎯 Using default coordinates - Nest: {nest_coords}, Mouse: {mouse_coords}")
        
        # Send frame extraction notification
        send_processing_notification(video_name, video_path, "processing", "extract", job_id)
        
        # Run the Linux Mint processing script
        cmd = [
            'python3',
            '/home/morsestudio/sam2/videologic/process_video_linux.py',
            '--video_path', video_path,
            '--nest_x', str(nest_coords[0]),
            '--nest_y', str(nest_coords[1]),
            '--mouse_x', str(mouse_coords[0]),
            '--mouse_y', str(mouse_coords[1]),
            '--output_dir', '/home/morsestudio/sam2/results'
        ]
        
        # Send segmentation start notification
        send_processing_notification(video_name, video_path, "processing", "segment", job_id)
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Auto-processing completed for {video_name}")
        print(f"📊 Output: {result.stdout}")
        
        # Send completion notification to Mac backend
        send_processing_notification(video_name, video_path, "completed", "complete", job_id)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Auto-processing failed for {video_name}: {e}")
        print(f"Error output: {e.stderr}")
        send_processing_notification(video_name, video_path, "failed", "segment", job_id)
        return False
    except Exception as e:
        print(f"❌ Error in auto-processing {video_name}: {e}")
        send_processing_notification(video_name, video_path, "failed", "segment", job_id)
        return False

def send_processing_notification(filename, filepath, status, step=None, job_id=None):
    """Send processing completion notification to Mac backend"""
    try:
        payload = {
            "filename": filename,
            "filepath": filepath,
            "status": status,
            "timestamp": int(time.time()),
            "type": "video_processing",
            "step": step,
            "jobId": job_id
        }
        response = requests.post(WEBHOOK_URL.replace('/download-complete', '/processing-complete'), json=payload)
        response.raise_for_status()
        print(f"🔔 Processing notification sent for {filename}: {status} - {step}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Warning: Could not send processing notification for {filename}: {e}")

if __name__ == "__main__":
    print("🚀 TaiLOR Google Drive Download Script (Fully Automated)")
    print(f"📁 Downloading from folder: {DRIVE_FOLDER_ID}")
    print(f"💾 Saving to: {DOWNLOAD_DIR}")
    print()
    
    download_files_from_drive()
