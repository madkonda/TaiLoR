# Google Drive Picker Setup

## What Was Added

✅ **Backend endpoint**: `/api/process-drive-file` - Downloads files from Drive and processes them
✅ **Frontend button**: "Select from Google Drive" - Opens Google Picker
✅ **File naming**: Preserves original filename for organized folder structure

## How It Works

1. **User clicks "Select from Google Drive"**
   - Google Picker opens
   - User selects video file from their Drive
   
2. **Frontend sends file ID to backend**
   - Backend downloads file from Drive
   - Preserves original filename (e.g., `1.mp4`)
   
3. **Backend uploads to processing folder**
   - File goes to `TaiLOR/videos/1.mp4` (keeps original name)
   - Linux Mint processes it
   - Creates `results/1/` folder (named after video)
   
4. **Results organized by video name**
   - Video: `1.mp4` → Folder: `results/1/`
   - All outputs in organized structure

## Setup Steps

### 1. Get Google API Credentials

1. Go to: https://console.cloud.google.com/apis/credentials
2. Create API Key:
   - Click "Create Credentials" → "API Key"
   - Copy the key
3. Enable APIs:
   - Enable "Google Picker API"
   - Enable "Google Drive API"

### 2. Add to Frontend Environment

Create `frontend/.env.local`:
```env
VITE_GOOGLE_API_KEY=your_api_key_here
VITE_GOOGLE_CLIENT_ID=your_client_id_here
```

### 3. Update Vercel (Production)

In Vercel Dashboard → Your Project → Settings → Environment Variables:
- Add: `VITE_GOOGLE_API_KEY` = your API key
- Add: `VITE_GOOGLE_CLIENT_ID` = your client ID

### 4. Restart Frontend

```bash
cd frontend
npm run dev
```

## File Naming Behavior

**Upload method:**
- User uploads `1.mp4`
- Backend saves as `1.mp4` (keeps original name)
- Results in `results/1/`

**Drive Picker method:**
- User selects `1.mp4` from Drive
- Backend downloads and saves as `1.mp4` (preserves original name)
- Results in `results/1/`

**Both methods preserve filename!** ✅

## Benefits

- ✅ **Two options**: Upload OR select from Drive
- ✅ **Consistent naming**: Both methods use original filename
- ✅ **Organized results**: Folder structure matches video name
- ✅ **No upload bandwidth**: Drive files don't need re-uploading

## Testing

1. Without API key: Upload button still works ✅
2. With API key: Both buttons work ✅

The Drive Picker button will show an alert if not configured - upload option always works!

