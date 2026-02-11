import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { ensureGoogleIdentity, ensureGapiClient } from '../utils/googleApi';

interface GoogleUserProfile {
  email: string;
  name?: string;
  picture?: string;
}

export interface UseGoogleAuthConfig {
  clientId: string;
  scopes: string[];
}

interface UseGoogleAuthResult {
  isReady: boolean;
  isAuthenticated: boolean;
  accessToken: string | null;
  user: GoogleUserProfile | null;
  signIn: () => void;
  signOut: () => void;
  refreshToken: () => void;
}

const STORAGE_KEY_TOKEN = 'tailor_auth_token';
const STORAGE_KEY_USER = 'tailor_auth_user';

export const useGoogleAuth = (config: UseGoogleAuthConfig): UseGoogleAuthResult => {
  const [isReady, setIsReady] = useState(false);
  const [accessToken, setAccessToken] = useState<string | null>(() => {
    // Restore from localStorage on mount
    try {
      const stored = localStorage.getItem(STORAGE_KEY_TOKEN);
      return stored || null;
    } catch {
      return null;
    }
  });
  const [user, setUser] = useState<GoogleUserProfile | null>(() => {
    // Restore from localStorage on mount
    try {
      const stored = localStorage.getItem(STORAGE_KEY_USER);
      return stored ? JSON.parse(stored) : null;
    } catch {
      return null;
    }
  });
  const tokenClientRef = useRef<any>(null);
  const fetchingProfileRef = useRef<boolean>(false);
  const lastValidTokenRef = useRef<string | null>(null); // Track last valid token from callback
  const scopes = useMemo(() => config.scopes.join(' '), [config.scopes]);

  const fetchProfile = useCallback(async (token: string, skipIfFetching = true) => {
    if (!token) {
      console.warn('No token provided to fetchProfile');
      return;
    }

    // Only fetch profile if this is the last valid token we received from callback
    if (lastValidTokenRef.current && token !== lastValidTokenRef.current) {
      console.warn('⚠️ Ignoring fetchProfile call - token does not match last valid token from callback');
      return;
    }

    // Prevent concurrent profile fetches (unless explicitly allowed)
    if (skipIfFetching && fetchingProfileRef.current) {
      console.log('Profile fetch already in progress, skipping...');
      return;
    }

    fetchingProfileRef.current = true;

    console.log('🔍 Fetching user profile with token:', token.substring(0, 20) + '...');

    try {
      const response = await fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      if (!response.ok) {
        if (response.status === 401) {
          const errorBody = await response.json().catch(() => ({}));
          console.error('❌ Token invalid (401):', errorBody);
          console.warn('Token that failed:', token.substring(0, 30) + '...');
          console.warn('Last valid token from callback:', lastValidTokenRef.current?.substring(0, 30) + '...' || 'none');
          console.warn('Clearing invalid token - please sign in again');
          
          // Clear tokens
          lastValidTokenRef.current = null;
          setAccessToken(null);
          setUser(null);
          // Clear localStorage
          try {
            localStorage.removeItem(STORAGE_KEY_TOKEN);
            localStorage.removeItem(STORAGE_KEY_USER);
          } catch (e) {
            console.warn('Failed to clear localStorage:', e);
          }
          
          // Don't auto-refresh to avoid loops - user needs to click sign in again
          if (errorBody.error === 'invalid_request' && errorBody.error_description?.includes('Invalid Credentials')) {
            alert('Authentication failed. Please check:\n1. OAuth Consent Screen is configured\n2. Your email is added as a test user (if app is in Testing mode)\n3. Try signing in again');
          } else {
            alert('Session expired. Please sign in again.');
          }
        } else {
          const errorText = await response.text().catch(() => 'Unknown error');
          console.error(`Failed to retrieve user profile: ${response.status}`, errorText);
        }
        return;
      }

      const data = await response.json();
      console.log('✅ Profile loaded successfully:', data.email);
      const userProfile = {
        email: data.email,
        name: data.name,
        picture: data.picture
      };
      setUser(userProfile);
      // Persist to localStorage
      try {
        localStorage.setItem(STORAGE_KEY_USER, JSON.stringify(userProfile));
      } catch (e) {
        console.warn('Failed to persist user to localStorage:', e);
      }
    } catch (error) {
      console.error('Error fetching user profile:', error);
      // Don't throw - allow app to continue without profile
    } finally {
      fetchingProfileRef.current = false;
    }
  }, []);

  const initClient = useCallback(async () => {
    await ensureGapiClient();

    const identity = await ensureGoogleIdentity();
    if (!identity) {
      throw new Error('Google Identity Services failed to load.');
    }

    if (!config.clientId) {
      console.error('Google Client ID is missing!');
      setIsReady(true); // Still set ready so UI can show error
      return;
    }

    // Get current origin for logging
    const currentOrigin = typeof window !== 'undefined' ? window.location.origin : 'http://localhost:5173';
    console.log('🔧 Initializing token client');
    console.log('   Client ID:', config.clientId.substring(0, 30) + '...');
    console.log('   Origin:', currentOrigin);
    console.log('   Scopes:', scopes);

    // Note: Google Identity Services automatically handles redirect URIs
    // Do NOT specify redirect_uri here - it's handled by GIS
    tokenClientRef.current = identity.oauth2.initTokenClient({
      client_id: config.clientId,
      scope: scopes,
      callback: (tokenResponse: any) => {
        console.log('Token callback received:', {
          hasAccessToken: !!tokenResponse?.access_token,
          error: tokenResponse?.error,
          errorDescription: tokenResponse?.error_description,
          scope: tokenResponse?.scope
        });

        if (tokenResponse?.access_token) {
          const token = tokenResponse.access_token;
          console.log('✅ Token received successfully');
          console.log('Token length:', token.length);
          console.log('Token preview:', token.substring(0, 30) + '...');
          const grantedScopes = tokenResponse.scope ? tokenResponse.scope.split(' ') : [];
          console.log('Scopes granted:', grantedScopes);
          console.log('Scopes requested:', scopes.split(' '));
          
          // Warn if critical scopes are missing
          const requiredScopes = ['openid', 'email', 'profile'];
          const missingScopes = requiredScopes.filter(s => !grantedScopes.includes(s));
          if (missingScopes.length > 0) {
            console.warn('⚠️ Missing required scopes:', missingScopes);
            console.warn('   These scopes must be added to OAuth Consent Screen in Console');
          }
          
          // Validate token format (should be a JWT or OAuth token string)
          if (!token || token.length < 20) {
            console.error('❌ Token appears invalid (too short)');
            return;
          }
          
          // Store as last valid token
          lastValidTokenRef.current = token;
          setAccessToken(token);
          // Persist to localStorage
          try {
            localStorage.setItem(STORAGE_KEY_TOKEN, token);
          } catch (e) {
            console.warn('Failed to persist token to localStorage:', e);
          }
          
          // Wait a tiny bit to ensure state is set, then fetch profile
          setTimeout(() => {
            // Double-check we still have the same token
            if (lastValidTokenRef.current === token) {
              fetchProfile(token, false);
            } else {
              console.warn('⚠️ Token changed before profile fetch, skipping');
            }
          }, 100);
        } else if (tokenResponse?.error) {
          // Clear last valid token on error
          lastValidTokenRef.current = null;
          console.error('❌ Token error:', {
            error: tokenResponse.error,
            description: tokenResponse.error_description,
            details: tokenResponse.error_uri
          });
          setAccessToken(null);
          setUser(null);
          // Clear localStorage
          try {
            localStorage.removeItem(STORAGE_KEY_TOKEN);
            localStorage.removeItem(STORAGE_KEY_USER);
          } catch (e) {
            console.warn('Failed to clear localStorage:', e);
          }
          
          // If it's a consent error, guide user
          if (tokenResponse.error === 'access_denied') {
            console.warn('User denied consent');
            alert('Please grant all requested permissions to use this app.');
          } else if (tokenResponse.error === 'popup_closed_by_user') {
            console.warn('User closed the popup');
          } else {
            alert(`Authentication error: ${tokenResponse.error_description || tokenResponse.error}. Please try again.`);
          }
        } else {
          console.warn('Token callback received but no access_token or error');
        }
      }
    });

    console.log('Google Auth client initialized with client ID:', config.clientId.substring(0, 20) + '...');

    setIsReady(true);
  }, [config.clientId, fetchProfile, scopes]);

  useEffect(() => {
    initClient().catch((error: unknown) => {
      console.error(error);
    });
  }, [initClient]);

  // Validate stored token when ready
  useEffect(() => {
    if (isReady && accessToken && user) {
      // Token and user restored from localStorage, validate it
      lastValidTokenRef.current = accessToken;
      fetchProfile(accessToken, false);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isReady]); // Run when isReady becomes true

  const signIn = useCallback(() => {
    if (!tokenClientRef.current) {
      console.error('❌ Token client not initialized. Is Google Identity Services loaded?');
      alert('Google Identity Services not loaded. Please refresh the page.');
      return;
    }

    console.log('🔑 Requesting access token...', {
      clientId: config.clientId ? config.clientId.substring(0, 30) + '...' : 'MISSING',
      scopes: scopes
    });
    
    try {
      // Clear any existing token first
      setAccessToken(null);
      setUser(null);
      
      const currentOrigin = window.location.origin;
      console.log('🔑 Requesting token');
      console.log('   Origin:', currentOrigin);
      
      // Request token - don't force consent if user already authenticated before
      // Note: redirect_uri is automatically handled by Google Identity Services
      tokenClientRef.current.requestAccessToken({
        prompt: user ? '' : 'consent'
      });
    } catch (error) {
      console.error('❌ Error requesting access token:', error);
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      
      // Check for specific security errors
      if (errorMessage.includes('secure') || errorMessage.includes('browser')) {
        alert(
          'Google sign-in blocked. Please verify:\n\n' +
          '1. OAuth Client authorized JavaScript origins includes:\n   ' + window.location.origin + '\n\n' +
          '2. OAuth Client authorized redirect URIs includes:\n   ' + window.location.origin + '\n\n' +
          '3. Visit: https://console.cloud.google.com/apis/credentials (select your project)\n\n' +
          'Then try again.'
        );
      } else {
        alert(`Failed to start sign-in: ${errorMessage}`);
      }
    }
  }, [user, config.clientId, scopes]);

  const signOut = useCallback(() => {
    if (accessToken) {
      window.google?.accounts?.oauth2.revoke(accessToken);
    }
    setAccessToken(null);
    setUser(null);
    lastValidTokenRef.current = null; // Clear last valid token
    // Clear localStorage
    try {
      localStorage.removeItem(STORAGE_KEY_TOKEN);
      localStorage.removeItem(STORAGE_KEY_USER);
    } catch (e) {
      console.warn('Failed to clear localStorage:', e);
    }
  }, [accessToken]);

  const refreshToken = useCallback(() => {
    if (!tokenClientRef.current) {
      return;
    }

    tokenClientRef.current.requestAccessToken({ prompt: '' });
  }, []);

  return {
    isReady,
    isAuthenticated: Boolean(accessToken),
    accessToken,
    user,
    signIn,
    signOut,
    refreshToken
  };
};

