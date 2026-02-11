export interface DriveFile {
  id: string;
  name: string;
  mimeType?: string;
  webViewLink?: string;
  parents?: string[];
}

export interface TailorDriveStructure {
  rootId: string;
  videosId: string;
  resultsId: string;
}

export interface PickerSelection {
  id: string;
  name: string;
  url?: string;
  mimeType?: string;
}








