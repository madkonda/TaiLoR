# TaiLOR Backend Setup - Credentials

## Required Files

You need to create these files in the `backend/` directory:

### 1. `credentials.json`
Copy from `credentials.json.template` and fill in your Google OAuth2 credentials:
```bash
cp credentials.json.template credentials.json
# Edit credentials.json with your actual values
```

### 2. `service-account-key.json`
Copy from `service-account-key.json.template` and fill in your Google Service Account credentials:
```bash
cp service-account-key.json.template service-account-key.json
# Edit service-account-key.json with your actual values
```

### 3. `.env`
Copy from `env.example` and fill in your configuration:
```bash
cp env.example .env
# Edit .env with your actual values
```

## Getting Credentials

### Google OAuth2 Credentials (`credentials.json`)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Go to "APIs & Services" → "Credentials"
4. Create OAuth 2.0 Client ID (Web application)
5. Download the JSON file and rename to `credentials.json`

### Google Service Account (`service-account-key.json`)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Go to "APIs & Services" → "Credentials"
4. Create Service Account
5. Download the JSON key file and rename to `service-account-key.json`

## Security Note
⚠️ **NEVER commit these files to Git!** They contain sensitive credentials.
