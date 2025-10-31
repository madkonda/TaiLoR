#!/bin/bash
# Test API endpoint from different DNS servers

echo "Testing api.mintpc.morsestudio.dev..."
echo ""

echo "1. Testing via Cloudflare DNS (1.1.1.1):"
dig @1.1.1.1 api.mintpc.morsestudio.dev +short

echo ""
echo "2. Testing via Google DNS (8.8.8.8):"
dig @8.8.8.8 api.mintpc.morsestudio.dev +short

echo ""
echo "3. Testing connection (using dig result):"
IP=$(dig @1.1.1.1 api.mintpc.morsestudio.dev +short | head -1)
echo "Resolved to: $IP"

echo ""
echo "4. Testing from browser (open this in your browser):"
echo "https://api.mintpc.morsestudio.dev/api/health"
echo ""
echo "If browser works but curl doesn't, it's a local DNS cache issue."
echo "The API should work from tailor.morsestudio.dev once DNS propagates."

