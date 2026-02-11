export interface FrameExtractOptions {
  fps?: number;
  maxFrames?: number;
  onFrame?: (payload: FramePayload) => void | Promise<void>;
}

export interface FramePayload {
  blob: Blob;
  index: number;
  timestamp: number;
  totalEstimated: number;
}

const waitForEvent = (element: HTMLMediaElement, eventName: string): Promise<void> =>
  new Promise((resolve, reject) => {
    const onError = () => {
      cleanup();
      reject(new Error('Failed to load video for frame extraction.'));
    };

    const onEvent = () => {
      cleanup();
      resolve();
    };

    const cleanup = () => {
      element.removeEventListener(eventName, onEvent);
      element.removeEventListener('error', onError);
    };

    element.addEventListener(eventName, onEvent, { once: true });
    element.addEventListener('error', onError, { once: true });
  });

const seekTo = (video: HTMLVideoElement, time: number): Promise<void> =>
  new Promise((resolve, reject) => {
    const onSeeked = () => {
      cleanup();
      resolve();
    };

    const onError = () => {
      cleanup();
      reject(new Error('Failed to seek within the video.'));
    };

    const cleanup = () => {
      video.removeEventListener('seeked', onSeeked);
      video.removeEventListener('error', onError);
    };

    video.addEventListener('seeked', onSeeked, { once: true });
    video.addEventListener('error', onError, { once: true });
    video.currentTime = Math.min(time, video.duration || time);
  });

export const extractFrames = async (file: File, options: FrameExtractOptions = {}): Promise<void> => {
  const { fps = 1, maxFrames = 600, onFrame } = options;

  if (fps <= 0) {
    throw new Error('Frame extraction FPS must be greater than zero.');
  }

  const objectUrl = URL.createObjectURL(file);
  const video = document.createElement('video');
  video.src = objectUrl;
  video.crossOrigin = 'anonymous';
  video.muted = true;
  video.playsInline = true;

  try {
    await waitForEvent(video, 'loadedmetadata');

    const duration = video.duration;
    if (!duration || Number.isNaN(duration)) {
      throw new Error('Unable to determine video duration.');
    }

    // Extract every 10th frame: calculate effective frame interval
    const frameInterval = 1 / fps;
    const everyNthFrame = 10; // Extract every 10th frame
    
    // Calculate total frames considering we're sampling every 10th
    const totalFramesAtFps = Math.ceil(duration * fps);
    const totalEstimated = Math.min(Math.ceil(totalFramesAtFps / everyNthFrame), maxFrames);

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');

    if (!context) {
      throw new Error('Failed to create drawing context for frame extraction.');
    }

    let extractedIndex = 0; // Index for extracted frames (0, 1, 2, ...)
    let frameCounter = 0; // Counter for all frames at the specified FPS

    for (let timestamp = 0; timestamp <= duration && extractedIndex < totalEstimated; timestamp += frameInterval) {
      frameCounter += 1;
      
      // Only extract every 10th frame
      if (frameCounter % everyNthFrame !== 0) {
        continue;
      }

      await seekTo(video, timestamp);
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      const blob = await new Promise<Blob>((resolve, reject) => {
        canvas.toBlob((result) => {
          if (result) {
            resolve(result);
          } else {
            reject(new Error('Failed to generate image blob from canvas.'));
          }
        }, 'image/jpeg', 0.85);
      });

      await onFrame?.({
        blob,
        index: extractedIndex, // This will be used for padded naming (000000, 000001, etc.)
        timestamp,
        totalEstimated
      });

      extractedIndex += 1;
    }
  } finally {
    URL.revokeObjectURL(objectUrl);
  }
};

