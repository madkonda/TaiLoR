#!/usr/bin/env python3
"""
Create OAuth 2.0 Web Client for new project via IAM API
"""
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

# Set these for your deployment (do not commit real values if repo is public)
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "your-gcp-project-id")
CLIENT_NAME = "Tailor Web Client"
PRODUCTION_ORIGIN = os.environ.get("PRODUCTION_ORIGIN", "https://your-domain.com")
REDIRECT_URIS = [PRODUCTION_ORIGIN, "http://localhost:5173"]
JS_ORIGINS = [PRODUCTION_ORIGIN, "http://localhost:5173"]

def get_access_token():
    """Get access token from gcloud"""
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token", "--project", PROJECT_ID],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting access token: {e}", file=sys.stderr)
        sys.exit(1)

def create_oauth_client():
    """Try to create OAuth client via IAM API"""
    token = get_access_token()
    
    url = f"https://iam.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/oauthClients"
    
    data = {
        "displayName": CLIENT_NAME,
        "clientType": "WEB",
        "allowedRedirectUris": REDIRECT_URIS,
        "allowedJavascriptOrigins": JS_ORIGINS
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
            client_id = result.get("clientId", "")
            if client_id:
                print(f"\n✅ OAuth Client ID: {client_id}", file=sys.stderr)
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"HTTP Error {e.code}: {error_body}", file=sys.stderr)
        print("\n⚠️  OAuth Client creation via API failed.", file=sys.stderr)
        print("This must be created manually in the console:", file=sys.stderr)
        print(f"https://console.cloud.google.com/apis/credentials?project={PROJECT_ID}", file=sys.stderr)
        return None

if __name__ == "__main__":
    create_oauth_client()

