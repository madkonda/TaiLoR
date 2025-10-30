#!/usr/bin/env python3
"""
Test script to debug Linux server connection
"""

import requests
import json

def test_connection():
    urls = [
        'https://mintpc.morsestudio.dev/health',
        'https://mintpc.morsestudio.dev/list-files',
        'http://192.168.1.188:8080/health',
        'http://192.168.1.188:8080/list-files'
    ]
    
    for url in urls:
        try:
            print(f"🔍 Testing: {url}")
            response = requests.get(url, timeout=10)
            print(f"✅ Status: {response.status_code}")
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"📊 Data: {json.dumps(data, indent=2)}")
                except:
                    print(f"📄 Text: {response.text[:200]}...")
            else:
                print(f"❌ Error: {response.text[:200]}...")
        except Exception as e:
            print(f"❌ Exception: {e}")
        print("-" * 50)

if __name__ == "__main__":
    test_connection()


