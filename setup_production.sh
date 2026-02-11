#!/bin/bash
# One-time setup script for production deployment on GPU VM

set -e

# Set these for your deployment (do not commit real values if repo is public)
VM_USER="${VM_USER:-your-vm-username}"
VM_HOST="${VM_HOST:-your-vm-name}"
VM_ZONE="${VM_ZONE:-us-east1-d}"
VM_PROJECT="${VM_PROJECT:-your-gcp-project-id}"
DOMAIN="${DOMAIN:-your-domain.com}"

echo "🔧 Setting up production environment on GPU VM..."

# Install nginx and certbot
echo "📦 Installing nginx and certbot..."
gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="sudo apt-get update && sudo apt-get install -y nginx certbot python3-certbot-nginx"

# Create frontend directory
echo "📁 Creating frontend directory..."
gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="sudo mkdir -p /var/www/tailor-frontend && sudo chown -R $VM_USER:$VM_USER /var/www/tailor-frontend"

# Deploy nginx config
echo "⚙️  Configuring nginx..."
cat > /tmp/tailor-nginx.conf << EOF
server {
    listen 80;
    server_name ${DOMAIN};

    # Frontend static files
    location / {
        root /var/www/tailor-frontend;
        try_files $uri $uri/ /index.html;
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # Backend API proxy
    location /api {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        proxy_read_timeout 300s;
        proxy_connect_timeout 300s;
    }
}
EOF

# Use a safe filename for nginx site (replace dots with underscore if needed)
NGINX_SITE_NAME="${DOMAIN//./_}"

gcloud compute scp \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  /tmp/tailor-nginx.conf \
  $VM_USER@$VM_HOST:/tmp/tailor-nginx.conf

gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="sudo cp /tmp/tailor-nginx.conf /etc/nginx/sites-available/$NGINX_SITE_NAME && sudo ln -sf /etc/nginx/sites-available/$NGINX_SITE_NAME /etc/nginx/sites-enabled/ && sudo rm -f /etc/nginx/sites-enabled/default && sudo nginx -t && sudo systemctl reload nginx"

echo "✅ nginx configured"

# Set up systemd service for backend
echo "⚙️  Setting up backend systemd service..."
cat > /tmp/tailor-api.service << EOF
[Unit]
Description=Tailor SAM2 API Server
After=network.target

[Service]
Type=simple
User=$VM_USER
WorkingDirectory=/home/$VM_USER/sam2/backend
Environment="PATH=/home/$VM_USER/sam2/.venv/bin"
ExecStart=/home/$VM_USER/sam2/.venv/bin/python3 api_server.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

gcloud compute scp \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  /tmp/tailor-api.service \
  $VM_USER@$VM_HOST:/tmp/tailor-api.service

gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="sudo cp /tmp/tailor-api.service /etc/systemd/system/tailor-api.service && sudo systemctl daemon-reload && sudo systemctl enable tailor-api && sudo systemctl restart tailor-api && sudo systemctl status tailor-api --no-pager"

echo "✅ Backend service configured"

# Configure firewall
echo "🔥 Configuring firewall..."
gcloud compute firewall-rules create allow-http-https \
  --allow tcp:80,tcp:443 \
  --source-ranges 0.0.0.0/0 \
  --target-tags http-server,https-server \
  --project=$VM_PROJECT 2>/dev/null || echo "Firewall rule may already exist"

gcloud compute instances add-tags $VM_HOST \
  --tags=http-server,https-server \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT

echo "✅ Firewall configured"

echo ""
echo "✅ Production setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Point DNS: Add A record 'tailor' → $(gcloud compute instances describe $VM_HOST --zone=$VM_ZONE --project=$VM_PROJECT --format='get(networkInterfaces[0].accessConfigs[0].natIP)')"
echo "2. Run SSL: gcloud compute ssh $VM_HOST --zone=$VM_ZONE --project=$VM_PROJECT --command='sudo certbot --nginx -d $DOMAIN'"
echo "3. Deploy frontend: ./deploy_frontend.sh"
echo ""




