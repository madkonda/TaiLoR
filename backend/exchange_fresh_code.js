#!/usr/bin/env node

const { google } = require('googleapis');
require('dotenv').config();

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

// The fresh authorization code from the URL
const authCode = '4/0Ab32j91eZGeIW7w7o_BhC_2K7Bml14ICF3p-PrjYtyHrwtNs0Vts77PX6Cw9hkjvqyBkMA';

async function exchangeCodeForTokens() {
  try {
    console.log('🔄 Exchanging authorization code for tokens...');
    const { tokens } = await oauth2Client.getToken(authCode);
    
    console.log('✅ Successfully obtained tokens!');
    console.log('Refresh token:', tokens.refresh_token);
    console.log('Access token:', tokens.access_token);
    
    // Update .env file with refresh token
    const fs = require('fs');
    const envContent = fs.readFileSync('.env', 'utf8');
    
    // Remove existing refresh token if it exists
    const updatedEnv = envContent.replace(/GOOGLE_REFRESH_TOKEN=.*\n?/, '') + 
      `GOOGLE_REFRESH_TOKEN=${tokens.refresh_token}\n`;
    
    fs.writeFileSync('.env', updatedEnv);
    
    console.log('\n✅ .env file updated with refresh token!');
    console.log('🚀 You can now restart the backend and test file uploads.');
    
  } catch (error) {
    console.error('❌ Error exchanging code for tokens:', error.message);
    if (error.message.includes('invalid_grant')) {
      console.log('\n💡 The authorization code may have expired. Please get a fresh one.');
    }
  }
}

exchangeCodeForTokens();
