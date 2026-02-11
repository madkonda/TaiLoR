#!/usr/bin/env python3
"""
Create OAuth 2.0 Web Client via Google Cloud Console API
"""
import json
import subprocess
import sys
import urllib.request
import urllib.parse

PROJECT_ID = "tailor-app-new"
CLIENT_NAME = "Tailor Web Client"
REDIRECT_URIS = ["http://localhost:5173"]
JS_ORIGINS = ["http://localhost:5173"]

def get_access_token():
    """Get access token from gcloud"""
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting access token: {e}")
        sys.exit(1)

def create_oauth_client_via_console_api():
    """Try to create OAuth client via various API endpoints"""
    token = get_access_token()
    
    # Try the Cloud Console API endpoint
    url = f"https://console.cloud.google.com/apis/credentials/oauthclient/create"
    
    # Actually, we need to use the discovery API or IAM API
    # Let's try the IAM API with the proper endpoint
    url = f"https://iam.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/oauthClients"
    
    data = {
        "displayName": CLIENT_NAME,
        "redirectUris": REDIRECT_URIS,
        "javascriptOrigins": JS_ORIGINS,
        "type": "WEB"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print(json.dumps(result, indent=2))
            return result
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
        return None

if __name__ == "__main__":
    create_oauth_client_via_console_api()




