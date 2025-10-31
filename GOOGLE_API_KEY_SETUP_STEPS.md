# Google Drive Picker API Key Setup - Step by Step

## Current Status
You're on the Google Cloud Console Credentials page. You need to create an API Key.

## Step-by-Step Instructions

### Step 1: Create API Key
1. **Click the "Create Credentials" dropdown** (top of page)
2. **Select "API Key"**
3. A popup will appear with your API key - **COPY IT NOW** (you won't be able to see it again)

### Step 2: Restrict the API Key (Recommended)
1. In the API key popup, click **"Restrict key"**
2. Under **"API restrictions"**:
   - Select **"Restrict key"**
   - Check ONLY these APIs:
     - ✅ **Google Picker API**
     - ✅ **Google Drive API**
3. Under **"Application restrictions"**:
   - Select **"HTTP referrers (web sites)"**
   - Add these:
     - `https://tailor.morsestudio.dev/*`
     - `https://*.vercel.app/*`
     - `http://localhost:5173/*` (for local dev)
4. Click **"Save"**

### Step 3: Enable Required APIs
Before the API key works, you need to enable the APIs:

1. Go to **"APIs & Services"** → **"Library"** (left sidebar)
2. Search for **"Google Picker API"**:
   - Click it
   - Click **"Enable"**
3. Search for **"Google Drive API"**:
   - Click it
   - Click **"Enable"**

### Step 4: Add to Vercel
1. Go to **Vercel Dashboard**: https://vercel.com
2. Select your **"tailor"** project
3. Go to **Settings** → **Environment Variables**
4. Click **"Add New"**
5. Add:
   - **Key**: `VITE_GOOGLE_API_KEY`
   - **Value**: (paste the API key you copied)
   - **Environment**: Production, Preview, Development (select all)
6. Click **"Save"**

### Step 5: Redeploy
Vercel will auto-deploy, or manually trigger:
```bash
# In terminal:
cd /Users/madhukonda/TaiLOR
vercel --prod
```

## What You Already Have
- ✅ OAuth 2.0 Client ID: "TaiLOR File Upload" (for backend)
- ✅ Service Account: "tailor-backend" (for backend)
- ⏳ Need: API Key (for frontend Google Drive Picker)

## After Setup
Once you add the API key to Vercel and redeploy:
- ✅ Google Drive Picker button will become active (blue, clickable)
- ✅ Users can select videos from their Google Drive
- ✅ No more setup alert will appear

## Security Notes
- The API key is safe to expose in frontend code (it's meant to be public)
- It's restricted to only work on your domains
- It can only access Google Picker and Drive APIs
- Users will still need to authenticate with their Google account to access their Drive

