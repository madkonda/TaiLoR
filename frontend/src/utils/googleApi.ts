const DEFAULT_TIMEOUT = 20000;

const waitFor = <T>(getter: () => T | undefined, timeout = DEFAULT_TIMEOUT): Promise<T> =>
  new Promise((resolve, reject) => {
    const start = Date.now();

    const check = () => {
      const value = getter();
      if (value) {
        resolve(value);
        return;
      }

      if (Date.now() - start >= timeout) {
        reject(new Error('Timed out waiting for Google APIs to load.'));
        return;
      }

      window.setTimeout(check, 120);
    };

    check();
  });

let pickerPromise: Promise<void> | null = null;

export const ensurePickerLoaded = async (): Promise<void> => {
  if (pickerPromise) {
    return pickerPromise;
  }

  pickerPromise = (async () => {
    const gapiInstance = await waitFor(() => window.gapi);

    await new Promise<void>((resolve, reject) => {
      gapiInstance.load('picker', {
        callback: () => resolve(),
        onerror: () => reject(new Error('Failed to load Google Picker.')),
        timeout: DEFAULT_TIMEOUT,
        ontimeout: () => reject(new Error('Timed out loading Google Picker.'))
      });
    });
  })();

  return pickerPromise;
};

let clientPromise: Promise<void> | null = null;

export const ensureGapiClient = async (): Promise<void> => {
  if (clientPromise) {
    return clientPromise;
  }

  clientPromise = (async () => {
    await waitFor(() => window.gapi?.load);

    await new Promise<void>((resolve, reject) => {
      window.gapi.load('client', {
        callback: () => resolve(),
        onerror: () => reject(new Error('Failed to load gapi client.')),
        timeout: DEFAULT_TIMEOUT,
        ontimeout: () => reject(new Error('Timed out loading gapi client.'))
      });
    });
  })();

  return clientPromise;
};

export const ensureGoogleIdentity = async (): Promise<typeof window.google.accounts | null> => {
  const googleObj = await waitFor(() => window.google, DEFAULT_TIMEOUT).catch(() => null);
  return googleObj?.accounts ?? null;
};








