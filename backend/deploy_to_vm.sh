#!/bin/bash
# Deployment script to copy files to GCP VM

# Set these for your deployment
VM_USER="${VM_USER:-your-vm-username}"
VM_HOST="${VM_HOST:-your-vm-name}"
VM_ZONE="${VM_ZONE:-us-east1-d}"
VM_PROJECT="${VM_PROJECT:-your-gcp-project-id}"

echo "Deploying SAM2 service files to GCP VM..."

# Copy files to VM (to SAM2 backend directory)
TARGET_DIR="/home/$VM_USER/sam2/backend"

gcloud compute scp \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  backend/sam2_service.py \
  backend/api_server.py \
  backend/mouse_extraction.py \
  backend/rat_extraction.py \
  backend/rat2_extraction.py \
  backend/prediction.py \
  backend/review_flags.py \
  backend/fixed_points_configs/*.json \
  mouse_less_nest_tree_logic.py \
  mouse_nest_tree_logic.py \
  rat1_tree_logic.py \
  rat2_tree_logic.py \
  rat3_tree_logic.py \
  rat4_tree_logic.py \
  rat5_tree_logic.py \
  backend/requirements.txt \
  $VM_USER@$VM_HOST:$TARGET_DIR/

gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="mkdir -p $TARGET_DIR/fixed_points_configs"

gcloud compute scp \
  --recurse \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  backend/fixed_points_configs/* \
  $VM_USER@$VM_HOST:$TARGET_DIR/fixed_points_configs/

echo "Files deployed to /home/$VM_USER/sam2/backend/"
echo ""

echo "Restarting backend systemd service (tailor-api)..."
gcloud compute ssh $VM_USER@$VM_HOST \
  --zone=$VM_ZONE \
  --project=$VM_PROJECT \
  --command="sudo systemctl restart tailor-api && sudo systemctl status tailor-api --no-pager"

echo ""
echo "✅ Deployment complete. Backend service restarted."
echo "Note: SAM2_BASE_DIR defaults to ~/sam2, so no need to set it."

