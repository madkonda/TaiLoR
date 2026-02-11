# TAILOR

Video processing pipeline: upload videos to Google Drive, extract frames, run SAM2 segmentation (nest + subject), and store results.

## Repo layout

- **`frontend/`** — React + Vite app: Google sign-in, Drive upload, frame extraction, coordinate selection, SAM2 job submission. See [frontend/README.md](frontend/README.md).
- **`backend/`** — Flask API: SAM2 processing, async jobs, Drive integration, NPZ upload. See [backend/README.md](backend/README.md).

## Quick start

1. **Backend:** Python 3, install deps with `pip install -r backend/requirements.txt`. SAM2 and checkpoints must be set up on the machine (e.g. GCP VM).
2. **Frontend:** `cd frontend && npm install && npm run dev`. Configure OAuth Client ID and API key via `.env.local` (see frontend README).
3. **Deploy:** Use `backend/deploy_to_vm.sh` and `deploy_frontend.sh` for VM deploy; run `setup_production.sh` once on the VM for Nginx and systemd.

## Docs (root)

- [SYSTEM_DESIGN.md](SYSTEM_DESIGN.md) — Architecture, APIs, queue, tracking.
- [NEW_GMAIL_SETUP_GUIDE.md](NEW_GMAIL_SETUP_GUIDE.md) — GCP project and OAuth setup for a new account.

## License

Private / use as needed.
