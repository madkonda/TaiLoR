#!/usr/bin/env python3
"""
Create standard OAuth 2.0 Web client using Google API Client Library
This creates credentials compatible with Google Identity Services
"""
import json
import os
import subprocess
import sys

def run_command(cmd):
    """Run command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        return None

def main():
    """Create OAuth client via Google Cloud Console API"""
    project_id = os.environ.get("GCP_PROJECT_ID", "your-gcp-project-id")
    access_token = run_command("gcloud auth print-access-token")
    
    if not access_token:
        print("Failed to get access token", file=sys.stderr)
        sys.exit(1)
    
    # Try using the Cloud Console API for creating OAuth credentials
    # The endpoint is: https://console.cloud.google.com/apis/api/iamcredentials.googleapis.com
    # But actually we need the credentials API
    
    # Let's try the IAM Service Account Credentials API
    url = f"https://iamcredentials.googleapis.com/v1/projects/{project_id}/serviceAccounts/-:generateAccessToken"
    
    # Actually, OAuth client creation needs the Cloud Console API
    # Let's use the REST API discovery to find the right endpoint
    
    # The proper way: Use Google Cloud Console API
    # We'll use curl with the access token
    curl_cmd = f'''curl -s -X POST \\
  "https://console.cloud.google.com/apis/api/iamcredentials.googleapis.com" \\
  -H "Authorization: Bearer {access_token}" \\
  -H "Content-Type: application/json" \\
  -d '{{}}'
'''
    
    # Actually, let me try a different approach - use the API discovery
    print("Attempting to create OAuth 2.0 client...")
    print("Note: Standard OAuth 2.0 Web clients must be created via Google Cloud Console")
    print("The IAM OAuth clients don't support Drive scopes.")
    print()
    print("To create properly, visit:")
    print(f"https://console.cloud.google.com/apis/credentials?project={project_id}")
    print("Click 'Create Credentials' > 'OAuth client ID' > 'Web application'")
    print(f"Authorized JavaScript origins: http://localhost:5173")
    print(f"Authorized redirect URIs: http://localhost:5173")
    print()
    print("Then update frontend/.env.local with the Client ID (xxxxx.apps.googleusercontent.com)")
    
    return None

if __name__ == "__main__":
    main()





