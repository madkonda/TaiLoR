#!/bin/bash
# Deploy frontend to production VM

set -e

# Set these for your deployment (or leave unset to use placeholders)
VM_USER="${VM_USER:-your-vm-username}"
VM_HOST="${VM_HOST:-your-vm-name}"
VM_ZONE="${VM_ZONE:-us-east1-d}"
VM_PROJECT="${VM_PROJECT:-your-gcp-project-id}"
PRODUCTION_URL="${PRODUCTION_URL:-https://your-domain.com}"

echo "🚀 Building frontend for production..."

cd frontend

# Check if .env.production exists, if not use .env.local
if [ ! -f .env.production ]; then
    echo "⚠️  .env.production not found, using .env.local"
    if [ ! -f .env.local ]; then
        echo "❌ Error: Need either .env.production or .env.local"
        exit 1
    fi
    cp .env.local .env.production
fi

# Update SAM2 API URL for production
if grep -q "VITE_SAM2_API_URL" .env.production; then
    sed -i.bak "s|VITE_SAM2_API_URL=.*|VITE_SAM2_API_URL=${PRODUCTION_URL%/}/api|" .env.production
else
    echo "VITE_SAM2_API_URL=${PRODUCTION_URL%/}/api" >> .env.production
fi

# Build
echo "📦 Building with Vite..."
npm run build

if [ ! -d "dist" ]; then
    echo "❌ Build failed: dist/ directory not found"
    exit 1
fi

echo "✅ Build complete"

# Deploy to VM
echo "📤 Uploading to VM..."
cd dist
tar czf /tmp/tailor-frontend.tar.gz .
cd ..

gcloud compute scp \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  /tmp/tailor-frontend.tar.gz \
  $VM_USER@$VM_HOST:/tmp/

echo "🔄 Installing files on VM..."
gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="sudo rm -rf /var/www/tailor-frontend/* && cd /var/www/tailor-frontend && sudo tar xzf /tmp/tailor-frontend.tar.gz && sudo chown -R www-data:www-data /var/www/tailor-frontend && sudo systemctl reload nginx && rm /tmp/tailor-frontend.tar.gz"

rm /tmp/tailor-frontend.tar.gz

echo "✅ Frontend deployed successfully!"
echo "🌐 Open: $PRODUCTION_URL"

