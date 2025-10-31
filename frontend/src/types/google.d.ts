// TypeScript declarations for Google Picker API

interface Window {
  google?: {
    accounts?: {
      oauth2?: {
        initTokenClient: (config: {
          client_id: string;
          scope: string;
          prompt?: string;
          callback: (resp: { access_token?: string }) => void;
        }) => { requestAccessToken: () => void } | undefined;
      };
    };
    picker: {
      PickerBuilder: new () => GooglePickerBuilder;
      ViewId: {
        DOCS: string;
        VIDEOS: string;
      };
      Action: {
        PICKED: string;
      };
      Feature: {
        NAV_HIDDEN: string;
      };
    };
  };
  gapi?: {
    load: (api: string, config: { callback: () => void }) => void;
    picker?: any;
  };
}

interface GooglePickerBuilder {
  setOAuthToken?(token: string): GooglePickerBuilder;
  setDeveloperKey(key: string): GooglePickerBuilder;
  setCallback(callback: (data: { action: string; docs: Array<{ id: string; name: string }> }) => void): GooglePickerBuilder;
  addView(viewId: string): GooglePickerBuilder;
  setSelectableMimeTypes(mimeTypes: string): GooglePickerBuilder;
  enableFeature(feature: string): GooglePickerBuilder;
  build(): GooglePicker;
}

interface GooglePicker {
  setVisible(visible: boolean): void;
}

