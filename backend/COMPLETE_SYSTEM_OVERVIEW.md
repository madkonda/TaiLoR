# TaiLOR Complete System Overview

## 🎯 System Architecture

TaiLOR is a complete end-to-end video processing system that automatically handles mouse behavior video analysis using SAM2 (Segment Anything Model 2). The system consists of:

### Frontend (React + TypeScript + Vite)
- **Deployed at**: `https://tailor.morsestudio.dev`
- **Features**:
  - Beautiful drag-and-drop video upload interface
  - Real-time processing dashboard with live progress tracking
  - Linux Mint file system status monitoring
  - Coordinate input for nest and mouse positions
  - Support for files up to 5GB

### Mac Backend (Node.js + Express)
- **Port**: 3001
- **Features**:
  - Receives video uploads from frontend
  - Uploads files to Google Drive
  - Tracks processing jobs in real-time
  - Receives status updates from Linux Mint
  - Provides API endpoints for frontend polling

### Linux Mint Processing (Python + SAM2)
- **Features**:
  - Downloads videos from Google Drive automatically
  - Extracts frames using FFmpeg (every 10th frame at 30fps)
  - Performs SAM2 segmentation with nest and mouse coordinates
  - Sends real-time progress updates to Mac backend
  - Automatically deletes processed files from Google Drive

## 🚀 Complete Automation Flow

1. **Upload**: User uploads video via frontend
2. **Transfer**: Mac backend uploads to Google Drive
3. **Download**: Linux Mint automatically downloads from Google Drive
4. **Process**: Video is processed with SAM2 segmentation
5. **Cleanup**: Processed file is deleted from Google Drive
6. **Update**: Real-time status updates shown in frontend

## 📁 File Structure

```
TaiLOR/
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProcessingDashboard.tsx
│   │   │   └── LinuxStatusDashboard.tsx
│   │   ├── pages/
│   │   │   └── Upload.tsx
│   │   └── version.ts
│   └── vercel.json
├── backend/                     # Mac backend
│   ├── server.js               # Main Express server
│   ├── websocket_server.js     # WebSocket server (deprecated)
│   ├── monitor_drive_continuous.py  # Continuous Google Drive monitoring
│   ├── process_video_linux.py  # SAM2 processing script
│   ├── linux_status.py         # Linux status monitoring
│   └── setup_*.sh             # Setup scripts
└── vercel.json                 # Vercel deployment config
```

## 🔧 Setup Instructions

### 1. Mac Backend Setup
```bash
cd backend
npm install
cp .env.example .env
# Edit .env with your Google Drive credentials
node server.js
```

### 2. Linux Mint Setup
```bash
# Copy files to Linux Mint
scp -r backend/ morsestudio@morsestudio:~/sam2/

# On Linux Mint, run setup scripts
cd ~/sam2/backend
chmod +x setup_continuous_monitoring.sh
./setup_continuous_monitoring.sh
```

### 3. Google Drive Configuration
1. Create Google Cloud Project
2. Enable Google Drive API
3. Create Service Account
4. Download credentials as `service-account-key.json`
5. Share Google Drive folder with service account email

## 🎛️ Real-time Features

### Processing Dashboard
- Shows active processing jobs
- Real-time progress updates
- Step-by-step status tracking
- Visual progress bars

### Linux Status Dashboard
- Live file system monitoring
- Shows videos in input directory
- Displays processing and completed files
- Real-time updates every 3 seconds

## 🔄 API Endpoints

### Mac Backend (Port 3001)
- `POST /api/upload` - Upload videos to Google Drive
- `GET /api/jobs` - Get all processing jobs
- `GET /api/jobs/:jobId` - Get specific job status
- `GET /api/linux-status` - Get Linux Mint status
- `POST /api/linux-status-update` - Receive Linux updates
- `POST /api/processing-complete` - Receive processing notifications

## 🎬 Video Processing Pipeline

1. **Frame Extraction**: FFmpeg extracts every 10th frame (3fps from 30fps)
2. **SAM2 Initialization**: Loads SAM2 model with Hiera-L configuration
3. **Point Prompts**: Uses nest (677, 881) and mouse (766, 773) coordinates
4. **Segmentation**: Propagates masks through all frames
5. **Output**: Saves masks as NPZ files in results directory

## 🗑️ Automatic Cleanup

- Files are automatically deleted from Google Drive after successful processing
- Failed processing jobs keep files in Google Drive for retry
- Non-video files are deleted immediately after download
- Local files remain on Linux Mint for analysis

## 📊 Monitoring & Logging

### Systemd Services
- `tailor-drive-monitor.service` - Continuous Google Drive monitoring
- `tailor-linux-monitor.service` - Linux status monitoring

### Logs
```bash
# View monitoring logs
sudo journalctl -u tailor-drive-monitor -f

# View Linux status logs
sudo journalctl -u tailor-linux-monitor -f
```

## 🎨 Frontend Features

### Upload Interface
- Drag-and-drop zone
- Click to select files
- File size validation (5GB limit)
- Multiple file support
- Coordinate input modal

### Real-time Dashboards
- Processing job tracking
- Linux file system status
- Connection status indicators
- Progress bars and status icons

## 🔐 Security

- Google Drive credentials stored securely
- Service account authentication
- No sensitive data in Git repository
- Template files for easy setup

## 🚀 Deployment

### Frontend
- Automatically deployed to Vercel
- Custom domain: `tailor.morsestudio.dev`
- Static site with SPA routing

### Backend
- Runs locally on Mac
- Connects to Linux Mint via Google Drive
- Real-time communication via HTTP polling

## 📈 Performance

- Supports videos up to 5GB
- Real-time processing updates
- Efficient frame extraction (3fps)
- Automatic cleanup prevents storage bloat
- Parallel processing support

## 🎯 Key Benefits

1. **Fully Automated**: Upload once, everything else is automatic
2. **Real-time Updates**: See progress as it happens
3. **Scalable**: Can process multiple videos simultaneously
4. **Clean**: Automatic file cleanup prevents storage issues
5. **User-friendly**: Beautiful interface with clear status indicators
6. **Robust**: Error handling and retry mechanisms

## 🔧 Troubleshooting

### Common Issues
1. **File size limit**: Ensure 5GB limit is configured
2. **Google Drive access**: Check service account permissions
3. **Linux connection**: Verify IP address in scripts
4. **SAM2 errors**: Check model files and conda environment

### Debug Commands
```bash
# Check service status
sudo systemctl status tailor-drive-monitor

# View logs
sudo journalctl -u tailor-drive-monitor -f

# Test Google Drive access
python3 monitor_drive_continuous.py
```

This system provides a complete, automated solution for mouse behavior video analysis with real-time monitoring and beautiful user interface.


