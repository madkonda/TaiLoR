#!/usr/bin/env node

const { google } = require('googleapis');
const readline = require('readline');
require('dotenv').config();

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  'urn:ietf:wg:oauth:2.0:oob' // This is a special redirect URI for desktop apps
);

// Generate the URL for OAuth2 consent
const authUrl = oauth2Client.generateAuthUrl({
  access_type: 'offline',
  scope: ['https://www.googleapis.com/auth/drive.file']
});

console.log('🔗 Open this URL in your browser:');
console.log(authUrl);
console.log('\n📋 After authorization, you\'ll get a code. Paste it here:');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Authorization code: ', async (code) => {
  try {
    const { tokens } = await oauth2Client.getToken(code);
    console.log('\n✅ Refresh token obtained!');
    console.log('Refresh token:', tokens.refresh_token);
    console.log('\n📝 Add this to your .env file:');
    console.log(`GOOGLE_REFRESH_TOKEN=${tokens.refresh_token}`);
    
    // Update .env file
    const fs = require('fs');
    const envContent = fs.readFileSync('.env', 'utf8');
    const updatedEnv = envContent + `\nGOOGLE_REFRESH_TOKEN=${tokens.refresh_token}`;
    fs.writeFileSync('.env', updatedEnv);
    
    console.log('\n✅ .env file updated automatically!');
    console.log('🚀 You can now restart the backend and test file uploads.');
    
  } catch (error) {
    console.error('❌ Error getting refresh token:', error.message);
  }
  
  rl.close();
});
