# Tailor Drive Uploader

React + Vite front-end that lets you:

- Sign in with Google and request Drive access using Google Identity Services.
- Upload a local video into your Google Drive folder structure `tailor/videos`.
- Extract frames in the browser (configurable FPS & max frames) and store them in `tailor/results/<video-name>`.
- Browse everything you've uploaded with the Google Picker dialog.

> Frame extraction happens client-side using `<video>` + `<canvas>` so large videos can take time. The UI streams each frame back to Drive sequentially.

## Prerequisites

1. Enable these APIs in the Google Cloud project you saw in `gcloud auth list` (or create a project):
   - Google Drive API
   - Google Picker API
   - Google Identity Services
2. **IMPORTANT**: Create a standard **OAuth 2.0 Web client** via Google Cloud Console (this cannot be done via CLI):
   - Go to: https://console.cloud.google.com/apis/credentials (select your project)
   - Click "Create Credentials" → "OAuth client ID"
   - Application type: "Web application"
   - Name: "Tailor Web Client"
   - Authorized JavaScript origins: `http://localhost:5173`
   - Authorized redirect URIs: `http://localhost:5173`
   - Copy the **Client ID** (format: `xxxxx.apps.googleusercontent.com`)
   - Note: The IAM OAuth clients created via `gcloud alpha iam oauth-clients` don't work with Google Identity Services
3. Create an **API key** in the same credentials page (Credentials → Create credentials → API key). Restrict it to Drive and Picker APIs.
4. Copy your **project number** (Project settings in Console, or `gcloud projects describe YOUR_PROJECT_ID --format='value(projectNumber)'`).

## Configuration

Create `frontend/.env.local` with:

```
VITE_GOOGLE_CLIENT_ID=your-oauth-client-id.apps.googleusercontent.com
VITE_GOOGLE_API_KEY=your_public_api_key
VITE_GOOGLE_APP_ID=your_project_number
```

Never commit the `.env.local` file; it contains credentials.

## Install & run (after you regain network access)

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173`.

## How it works

- `useGoogleAuth` loads Google Identity Services and manages OAuth tokens.
- `useDrive` wraps Drive REST calls to create the folder hierarchy, upload videos, and stream frame uploads.
- `extractFrames` (in `src/utils/frameExtractor.ts`) leverages the browser video element and canvas to capture frames at the chosen FPS.
- Google Picker loads via `gapi.load('picker')` and is scoped to the `tailor/videos` or `tailor/results` folders.

The activity log shows progress throughout uploads. Errors bubble into the log and a toast alert.

## Notes & limits

- Processing happens entirely in the browser; very long or high-resolution videos can stress the client.
- If you need server-side processing, plug the upload callback into a Cloud Run/Functions service and skip client-side frame extraction.
- Drive quotas apply; uploading many frames quickly may trigger `403 rateLimitExceeded` errors—respect the log if it happens.

## Next steps

- Add retry logic for transient Drive errors.
- If you need more control over Picker results, persist the selected IDs and load metadata via Drive v3.
- Build a simple backend to offload frame processing when browser performance is insufficient.

