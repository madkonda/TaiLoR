#!/usr/bin/env python3
"""
TaiLOR Google Drive Download Script for Linux Mint
Downloads files from Google Drive folder to local directory
"""

import os
import sys
import json
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Configuration
DRIVE_FOLDER_ID = "1HvGlLB-MjcYftrQ-SHeopc913vSEUNKA"  # Your Google Drive folder ID
DOWNLOAD_DIR = "/home/morsestudio/sam2/videos"  # Local download directory

def get_credentials():
    """Get valid user credentials from storage or run OAuth flow."""
    creds = None
    token_file = 'token.json'
    
    # Load existing credentials
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # You'll need to download the OAuth2 client credentials
            # and save them as 'credentials.json' in this directory
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    
    return creds

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
        
        print(f"\n🎉 All files downloaded to: {DOWNLOAD_DIR}")
        
    except Exception as e:
        print(f"❌ Error downloading files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🚀 TaiLOR Google Drive Download Script")
    print(f"📁 Downloading from folder: {DRIVE_FOLDER_ID}")
    print(f"💾 Saving to: {DOWNLOAD_DIR}")
    print()
    
    download_files_from_drive()
