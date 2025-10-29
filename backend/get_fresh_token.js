#!/usr/bin/env node

const { google } = require('googleapis');
const readline = require('readline');
require('dotenv').config();

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

// Generate a fresh authorization URL
const authUrl = oauth2Client.generateAuthUrl({
  access_type: 'offline',
  scope: ['https://www.googleapis.com/auth/drive.file'],
  prompt: 'consent' // This ensures we get a refresh token
});

console.log('🔗 Open this URL in your browser to get a fresh authorization code:');
console.log(authUrl);
console.log('\n📋 After authorization, you\'ll be redirected to:');
console.log('http://localhost:3001/auth/callback?code=XXXXX');
console.log('\n📋 Copy the code from the URL and paste it here:');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Authorization code: ', async (code) => {
  try {
    const { tokens } = await oauth2Client.getToken(code);
    console.log('\n✅ Successfully obtained tokens!');
    console.log('Refresh token:', tokens.refresh_token);
    
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
      console.log('\n💡 The authorization code may have expired. Please get a fresh one from the URL above.');
    }
  }
  
  rl.close();
});
