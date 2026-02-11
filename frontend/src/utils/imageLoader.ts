/**
 * Utility to load Google Drive images as blobs to avoid CORS issues
 * @param fileId - Google Drive file ID
 * @param accessToken - OAuth access token for authentication
 */
export async function loadDriveImageAsBlob(fileId: string, accessToken: string): Promise<string> {
  try {
    // Try using Authorization header (better security, but may have CORS restrictions)
    const response = await fetch(
      `https://www.googleapis.com/drive/v3/files/${fileId}?alt=media`,
      {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${accessToken}`
        },
        mode: 'cors' // Explicitly request CORS
      }
    );
    
    if (!response.ok) {
      // If 403/404, file might not be accessible with current token
      if (response.status === 403) {
        throw new Error(`Access denied (403). Check Drive API permissions and file sharing.`);
      }
      if (response.status === 404) {
        throw new Error(`File not found (404).`);
      }
      throw new Error(`Failed to fetch image: ${response.status} ${response.statusText}`);
    }
    
    const blob = await response.blob();
    return URL.createObjectURL(blob);
  } catch (error: any) {
    // If CORS error, try with query param (less secure but might work)
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      console.warn('CORS error with Authorization header, trying query param fallback...');
      try {
        const fallbackResponse = await fetch(
          `https://www.googleapis.com/drive/v3/files/${fileId}?alt=media&access_token=${accessToken}`,
          {
            mode: 'cors'
          }
        );
        
        if (!fallbackResponse.ok) {
          throw new Error(`Fallback failed: ${fallbackResponse.status} ${fallbackResponse.statusText}`);
        }
        
        const blob = await fallbackResponse.blob();
        return URL.createObjectURL(blob);
      } catch (fallbackError) {
        console.error('Fallback also failed:', fallbackError);
        throw new Error(`CORS policy blocked image loading. Google Drive API requires proper CORS configuration.`);
      }
    }
    
    console.error('Error loading image:', error);
    throw error;
  }
}

