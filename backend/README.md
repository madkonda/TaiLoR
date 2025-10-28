# TaiLOR Backend

Backend server for TaiLOR Mouse Behavior Analysis that uploads files to your Linux Mint PC via SFTP.

## Setup Instructions

### 1. Install Dependencies
```bash
cd backend
npm install
```

### 2. Configure Environment
```bash
cp env.example .env
```

Edit `.env` with your Linux Mint PC details:
```env
SFTP_HOST=192.168.1.100  # Your Linux Mint IP address
SFTP_USERNAME=morsestudio
SFTP_PASSWORD=your-password
SFTP_PORT=22
REMOTE_PATH=/home/morsestudio/sam2/notebooks/uploads
PORT=3001
```

### 3. Find Your Linux Mint IP Address
On your Linux Mint PC, run:
```bash
ip addr show | grep inet
```

### 4. Enable SSH on Linux Mint
```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

### 5. Create Upload Directory
```bash
mkdir -p /home/morsestudio/sam2/notebooks/uploads
chmod 755 /home/morsestudio/sam2/notebooks/uploads
```

### 6. Start the Backend
```bash
npm start
# or for development with auto-restart:
npm run dev
```

## API Endpoints

- `POST /api/upload` - Upload video files
- `GET /api/health` - Health check

## How It Works

1. Frontend uploads files to backend
2. Backend receives files via multer
3. Backend uploads files to Linux Mint PC via SFTP
4. Files are saved to `/home/morsestudio/sam2/notebooks/uploads/`
5. Local files are cleaned up after upload

## Testing

Test the backend:
```bash
curl http://localhost:3001/api/health
```

## Troubleshooting

- Make sure SSH is enabled on Linux Mint
- Check firewall settings
- Verify IP address and credentials
- Check file permissions on upload directory
