import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { extractFrames, FrameExtractOptions } from '../utils/frameExtractor';
import { ensurePickerLoaded } from '../utils/googleApi';
import { DriveFile, TailorDriveStructure, PickerSelection } from '../types';

interface UseDriveOptions {
  accessToken: string | null;
  apiKey: string;
  appId: string;
}

interface UploadResponse {
  id: string;
  name: string;
  webViewLink?: string;
}

interface UploadProgress {
  stage: 'idle' | 'ensure-folders' | 'upload-video' | 'extract-frames' | 'done';
  detail?: string;
  completedFrames?: number;
  totalFrames?: number;
}

export interface FrameFile {
  id: string;
  name: string;
}

export interface UseDriveReturn {
  structure: TailorDriveStructure | null;
  ensureStructure: () => Promise<TailorDriveStructure>;
  uploadVideo: (file: File) => Promise<UploadResponse>;
  uploadFramesFromVideo: (
    file: File,
    onProgress?: (progress: UploadProgress) => void,
    options?: FrameExtractOptions
  ) => Promise<{ videoFolderId: string; frameFolderId: string; videoName: string }>;
  openPicker: (view: 'videos' | 'results', onPicked: (selection: PickerSelection[]) => void) => Promise<void>;
  openFolderPicker: (parentFolderId: string, onPicked: (folderId: string, folderName: string) => void) => Promise<void>;
  resolveVideoFolder: (folderId: string) => Promise<{ videoFolderId: string; frameFolderId: string; videoName: string }>;
  getFrameFolderId: (baseName: string) => Promise<{ videoFolderId: string; frameFolderId: string } | null>;
  getFrameFiles: (folderId: string, limit?: number) => Promise<FrameFile[]>;
  getFileInfo: (fileId: string, fields?: string) => Promise<any>;
}

const DRIVE_API_BASE = 'https://www.googleapis.com/drive/v3/files';
const DRIVE_UPLOAD_BASE = 'https://www.googleapis.com/upload/drive/v3/files';

const FOLDER_MIME = 'application/vnd.google-apps.folder';
const ROOT_FOLDER = 'tailor';
const VIDEOS_FOLDER = 'videos';
const RESULTS_FOLDER = 'results';

const decodeError = async (response: Response): Promise<Error> => {
  let message = `${response.status} ${response.statusText}`;
  try {
    const data = await response.json();
    if (data?.error?.message) {
      message = data.error.message;
    }
  } catch (err) {
    console.error('Failed to decode Drive error', err);
  }
  return new Error(`Google Drive error: ${message}`);
};

export const useDrive = ({ accessToken, apiKey, appId }: UseDriveOptions): UseDriveReturn => {
  const [structure, setStructure] = useState<TailorDriveStructure | null>(null);
  const structurePromiseRef = useRef<Promise<TailorDriveStructure> | null>(null);

  const authHeader = useMemo(() => {
    if (!accessToken) {
      return null;
    }
    return { Authorization: `Bearer ${accessToken}` } as const;
  }, [accessToken]);

  const request = useCallback(
    async (input: string, init: RequestInit = {}) => {
      if (!authHeader) {
        throw new Error('Google Drive access token is missing. Please sign in again.');
      }

      const response = await fetch(input, {
        ...init,
        headers: {
          ...(init.headers || {}),
          ...authHeader
        }
      });

      if (!response.ok) {
        throw await decodeError(response);
      }

      return response;
    },
    [authHeader]
  );

  const listByName = useCallback(
    async (name: string, parent?: string): Promise<DriveFile | null> => {
      const filters = [`name = '${name.replace(/'/g, "\\'")}'`, `mimeType = '${FOLDER_MIME}'`, 'trashed = false'];
      if (parent) {
        filters.push(`'${parent}' in parents`);
      }

      const response = await request(
        `${DRIVE_API_BASE}?q=${encodeURIComponent(filters.join(' and '))}&fields=files(id,name,parents)&pageSize=1`
      );
      const data = await response.json();
      return data.files?.[0] ?? null;
    },
    [request]
  );

  const createFolder = useCallback(
    async (name: string, parent?: string): Promise<DriveFile> => {
      const response = await request(DRIVE_API_BASE, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name,
          mimeType: FOLDER_MIME,
          parents: parent ? [parent] : undefined
        })
      });

      return response.json();
    },
    [request]
  );

  const ensureFolder = useCallback(
    async (name: string, parent?: string) => {
      const existing = await listByName(name, parent);
      if (existing) {
        return existing.id;
      }
      const created = await createFolder(name, parent);
      return created.id;
    },
    [createFolder, listByName]
  );

  const listFilesInFolder = useCallback(
    async (parentId: string, mimeType?: string): Promise<DriveFile[]> => {
      const filters = [`'${parentId}' in parents`, 'trashed = false'];
      if (mimeType) {
        filters.push(`mimeType = '${mimeType}'`);
      }
      const response = await request(
        `${DRIVE_API_BASE}?q=${encodeURIComponent(filters.join(' and '))}&fields=files(id,name,mimeType)&pageSize=1000`
      );
      const data = await response.json();
      return data.files || [];
    },
    [request]
  );

  const deleteFile = useCallback(
    async (fileId: string): Promise<void> => {
      await request(`${DRIVE_API_BASE}/${fileId}`, {
        method: 'DELETE'
      });
    },
    [request]
  );

  const clearFolder = useCallback(
    async (folderId: string): Promise<void> => {
      const files = await listFilesInFolder(folderId);
      if (files.length === 0) {
        return;
      }

      await Promise.all(files.map((file) => deleteFile(file.id)));
    },
    [listFilesInFolder, deleteFile]
  );

  const getFileInfo = useCallback(
    async (fileId: string, fields: string = 'id,name,parents,mimeType'): Promise<any> => {
      const response = await request(`${DRIVE_API_BASE}/${fileId}?fields=${fields}`);
      return response.json();
    },
    [request]
  );

  const ensureStructureInternal = useCallback(async (): Promise<TailorDriveStructure> => {
    const rootId = await ensureFolder(ROOT_FOLDER);
    const videosId = await ensureFolder(VIDEOS_FOLDER, rootId);
    const resultsId = await ensureFolder(RESULTS_FOLDER, rootId);

    return { rootId, videosId, resultsId };
  }, [ensureFolder]);

  const ensureStructure = useCallback(async () => {
    if (!structurePromiseRef.current) {
      structurePromiseRef.current = ensureStructureInternal().then((result) => {
        setStructure(result);
        return result;
      });
    }

    return structurePromiseRef.current;
  }, [ensureStructureInternal]);

  useEffect(() => {
    if (!accessToken) {
      structurePromiseRef.current = null;
      setStructure(null);
    }
  }, [accessToken]);

  const uploadMultipart = useCallback(
    async (blob: Blob, metadata: Record<string, unknown>): Promise<UploadResponse> => {
      const formData = new FormData();
      formData.append('metadata', new Blob([JSON.stringify(metadata)], { type: 'application/json' }));
      formData.append('file', blob);

      const response = await request(`${DRIVE_UPLOAD_BASE}?uploadType=multipart&fields=id,name,webViewLink`, {
        method: 'POST',
        body: formData
      });

      return response.json();
    },
    [request]
  );

  const uploadVideo = useCallback(
    async (file: File): Promise<UploadResponse> => {
      const folders = await ensureStructure();

      return uploadMultipart(file, {
        name: file.name,
        mimeType: file.type || 'video/mp4',
        parents: [folders.videosId]
      });
    },
    [ensureStructure, uploadMultipart]
  );

  const uploadFramesFromVideo = useCallback(
    async (
      file: File,
      onProgress?: (progress: UploadProgress) => void,
      options?: FrameExtractOptions
    ): Promise<{ videoFolderId: string; frameFolderId: string; videoName: string }> => {
      const folders = await ensureStructure();
      const baseName = file.name.replace(/\.[^/.]+$/, '');

      const videoFolderId = await ensureFolder(baseName, folders.resultsId);
      const frameFolderId = await ensureFolder('frames', videoFolderId);

      // Remove any existing frames before uploading new ones
      await clearFolder(frameFolderId);

      const progressState: UploadProgress = { stage: 'extract-frames', completedFrames: 0, totalFrames: 0 };

      await extractFrames(file, {
        fps: options?.fps ?? 1,
        maxFrames: options?.maxFrames ?? 600,
        onFrame: async ({ blob, index, totalEstimated }) => {
          progressState.completedFrames = index + 1;
          progressState.totalFrames = totalEstimated;
          onProgress?.({ ...progressState, detail: `Uploading frame ${index + 1}/${totalEstimated}` });

          // Use padded 6-digit naming: 000000.jpg, 000001.jpg, etc.
          const paddedIndex = String(index).padStart(6, '0');
          await uploadMultipart(blob, {
            name: `${paddedIndex}.jpg`,
            mimeType: 'image/jpeg',
            parents: [frameFolderId]
          });
        }
      });

      onProgress?.({
        stage: 'done',
        detail: 'Frame extraction complete.',
        completedFrames: progressState.completedFrames,
        totalFrames: progressState.totalFrames
      });

      return { videoFolderId, frameFolderId, videoName: baseName };
    },
    [clearFolder, ensureFolder, ensureStructure, uploadMultipart]
  );

  const getFrameFolderId = useCallback(
    async (baseName: string): Promise<{ videoFolderId: string; frameFolderId: string } | null> => {
      const folders = await ensureStructure();
      const videoFolder = await listByName(baseName, folders.resultsId);
      if (!videoFolder) {
        return null;
      }

      const framesFolder = await listByName('frames', videoFolder.id);
      if (!framesFolder) {
        return null;
      }

      return { videoFolderId: videoFolder.id, frameFolderId: framesFolder.id };
    },
    [ensureStructure, listByName]
  );

  const resolveVideoFolder = useCallback(
    async (folderId: string): Promise<{ videoFolderId: string; frameFolderId: string; videoName: string }> => {
      const folderInfo = await getFileInfo(folderId, 'id,name,parents,mimeType');
      if (!folderInfo) {
        throw new Error('Could not load folder information.');
      }

      if (folderInfo.mimeType !== FOLDER_MIME) {
        throw new Error('Please select a folder.');
      }

      let videoFolderId: string | null = folderInfo.id ?? null;
      let videoName = folderInfo.name;
      let frameFolderId: string | null = null;

      if (!videoFolderId) {
        throw new Error('Selected folder has no ID.');
      }

      if (folderInfo.name === 'frames') {
        const parentId = folderInfo.parents?.[0];
        if (!parentId) {
          throw new Error('Frames folder has no parent.');
        }
        const parentInfo = await getFileInfo(parentId, 'id,name');
        videoFolderId = parentId;
        videoName = parentInfo.name ?? videoName;
        frameFolderId = folderInfo.id;
      } else {
        const framesFolder = await listByName('frames', videoFolderId);
        if (!framesFolder) {
          throw new Error('No "frames" subfolder found inside this video folder.');
        }
        frameFolderId = framesFolder.id;
      }

      if (!videoFolderId || !frameFolderId) {
        throw new Error('Unable to resolve video/frames folders.');
      }

      return { videoFolderId, frameFolderId, videoName };
    },
    [getFileInfo, listByName]
  );

  const getFrameFiles = useCallback(
    async (folderId: string, limit?: number): Promise<FrameFile[]> => {
      // Request file IDs and webContentLink (if available) for CORS fallback
      const response = await request(
        `${DRIVE_API_BASE}?q=${encodeURIComponent(`'${folderId}' in parents and mimeType='image/jpeg' and trashed=false`)}&fields=files(id,name,webContentLink)&orderBy=name`
      );
      const data = await response.json();
      const files: DriveFile[] = data.files || [];
      
      // Return file IDs - we'll try alt=media first, fallback to webContentLink if CORS fails
      const maxFiles = limit ?? files.length;
      return files.slice(0, maxFiles).map((file) => ({ id: file.id, name: file.name ?? '' }));
    },
    [request]
  );

  // New function to get a single frame URL (lazy loading)
  const getFrameUrl = useCallback(
    (fileId: string): string => {
      // Return file ID - we'll fetch with Authorization header to avoid CORS
      return fileId;
    },
    []
  );

  const openPicker = useCallback(
    async (viewType: 'videos' | 'results', onPicked: (selection: PickerSelection[]) => void) => {
      if (!accessToken) {
        throw new Error('You must be signed in to open Google Picker.');
      }

      const folders = await ensureStructure();

      await ensurePickerLoaded();

      const view = new google.picker.DocsView().setIncludeFolders(true).setSelectFolderEnabled(true);
      if (viewType === 'videos') {
        view.setParent(folders.videosId);
      } else {
        view.setParent(folders.resultsId);
      }

      const picker = new google.picker.PickerBuilder()
        .enableFeature(google.picker.Feature.NAV_HIDDEN)
        .enableFeature(google.picker.Feature.MULTISELECT_ENABLED)
        .setDeveloperKey(apiKey)
        .setAppId(appId)
        .setOAuthToken(accessToken)
        .addView(view)
        .setCallback((data: any) => {
          if (data.action === google.picker.Action.PICKED) {
            const docs: PickerSelection[] = data.docs?.map((doc: any) => ({
              id: doc.id,
              name: doc.name,
              url: doc.url,
              mimeType: doc.mimeType
            })) ?? [];
            onPicked(docs);
          }
        })
        .build();

      picker.setVisible(true);
    },
    [accessToken, apiKey, appId, ensureStructure]
  );

  const openFolderPicker = useCallback(
    async (parentFolderId: string, onPicked: (folderId: string, folderName: string) => void) => {
      if (!accessToken) {
        throw new Error('You must be signed in to open Google Picker.');
      }

      await ensurePickerLoaded();

      // Use DocsView to show folders
      const view = new google.picker.DocsView()
        .setIncludeFolders(true)
        .setSelectFolderEnabled(true)
        .setParent(parentFolderId)
        .setMimeTypes('application/vnd.google-apps.folder');

      const picker = new google.picker.PickerBuilder()
        .enableFeature(google.picker.Feature.NAV_HIDDEN)
        .setDeveloperKey(apiKey)
        .setAppId(appId)
        .setOAuthToken(accessToken)
        .addView(view)
        .setCallback((data: any) => {
          if (data.action === google.picker.Action.PICKED && data.docs?.[0]) {
            const folder = data.docs[0];
            onPicked(folder.id, folder.name);
          }
        })
        .build();

      picker.setVisible(true);
    },
    [accessToken, apiKey, appId]
  );

  return {
    structure,
    ensureStructure,
    uploadVideo,
    uploadFramesFromVideo,
    openPicker,
    openFolderPicker,
    resolveVideoFolder,
    getFrameFolderId,
    getFrameFiles,
    getFileInfo
  };
};

