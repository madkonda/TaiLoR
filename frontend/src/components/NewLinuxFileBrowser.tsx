import React, { useState, useEffect } from 'react';
import { apiUrl } from '../config';

interface FileInfo {
  name: string;
  path: string;
  size: number;
  modified: string;
  type: 'video' | 'directory';
}

interface FileData {
  videos: FileInfo[];
  results: FileInfo[];
  timestamp: string;
}

const NewLinuxFileBrowser: React.FC = () => {
  const [files, setFiles] = useState<FileData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [processing, setProcessing] = useState<string | null>(null);
  const [showCoordinateModal, setShowCoordinateModal] = useState(false);
  const [selectedFile, setSelectedFile] = useState<FileInfo | null>(null);
  const [coordinates, setCoordinates] = useState({
    nestX: 677,
    nestY: 881,
    mouseX: 766,
    mouseY: 773
  });

  const fetchFiles = async () => {
    try {
      setLoading(true);
      const response = await fetch(apiUrl('/list-files'));
      const data = await response.json();
      
      if (data.success) {
        setFiles(data.data);
        setError(null);
      } else {
        setError(data.error || 'Failed to fetch files');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchFiles();
    // Refresh every 5 seconds
    const interval = setInterval(fetchFiles, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleProcessVideo = async (file: FileInfo) => {
    setSelectedFile(file);
    setShowCoordinateModal(true);
  };

  const handleProcessConfirm = async () => {
    if (!selectedFile) return;
    
    setProcessing(selectedFile.name);
    try {
      console.log('🎬 Sending processing request:', {
        video_path: selectedFile.path,
        nest_x: coordinates.nestX,
        nest_y: coordinates.nestY,
        mouse_x: coordinates.mouseX,
        mouse_y: coordinates.mouseY
      });

      const response = await fetch(apiUrl('/process-video'), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          video_path: selectedFile.path,
          nest_x: coordinates.nestX,
          nest_y: coordinates.nestY,
          mouse_x: coordinates.mouseX,
          mouse_y: coordinates.mouseY
        })
      });

      console.log('📡 Response status:', response.status);
      console.log('📡 Response headers:', response.headers);

      if (!response.ok) {
        const errorText = await response.text();
        console.error('❌ Response error:', errorText);
        throw new Error(`HTTP ${response.status}: ${errorText}`);
      }

      const data = await response.json();
      console.log('📊 Response data:', data);
      
      if (data.success) {
        alert(`✅ Processing started for ${selectedFile.name}!\nNest: (${coordinates.nestX}, ${coordinates.nestY})\nMouse: (${coordinates.mouseX}, ${coordinates.mouseY})`);
        setShowCoordinateModal(false);
        setSelectedFile(null);
      } else {
        alert(`❌ Error: ${data.error}`);
      }
    } catch (err) {
      console.error('❌ Processing error:', err);
      alert(`❌ Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    } finally {
      setProcessing(null);
    }
  };

  const formatFileSize = (bytes: number) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const getFileIcon = (file: FileInfo) => {
    if (file.type === 'video') return '🎬';
    if (file.type === 'directory') return '📁';
    return '📄';
  };

  if (loading) {
    return (
      <div className="p-6 bg-gray-800 rounded-lg shadow-lg text-white text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
        <p>Loading files from Linux Mint...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-6 bg-red-900 rounded-lg shadow-lg text-white">
        <h2 className="text-2xl font-bold mb-4">❌ Error</h2>
        <p>{error}</p>
        <button 
          onClick={fetchFiles}
          className="mt-4 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="p-6 bg-gray-800 rounded-lg shadow-lg text-white">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-3xl font-bold">🐧 Linux Mint File Browser</h2>
        <button 
          onClick={fetchFiles}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          🔄 Refresh
        </button>
      </div>

      {files && (
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Videos */}
            <div className="bg-gray-700 p-4 rounded-lg">
              <h3 className="text-xl font-semibold mb-4 flex items-center">
                🎬 Videos ({files.videos.length})
              </h3>
              <div className="max-h-96 overflow-y-auto space-y-2">
                {files.videos.map((file, index) => (
                  <div key={index} className="flex items-center justify-between p-3 bg-gray-600 rounded group">
                    <div className="flex items-center gap-3 flex-1 min-w-0">
                      <span className="text-2xl">{getFileIcon(file)}</span>
                      <div className="flex-1 min-w-0">
                        <div className="font-mono text-sm truncate" title={file.path}>
                          {file.name}
                        </div>
                        <div className="text-xs text-gray-400 truncate" title={file.path}>
                          📁 {file.path}
                        </div>
                        <div className="text-xs text-gray-500">
                          📏 {formatFileSize(file.size)} • 🕒 {new Date(file.modified).toLocaleString()}
                        </div>
                      </div>
                    </div>
                    <button
                      onClick={() => handleProcessVideo(file)}
                      className="opacity-0 group-hover:opacity-100 bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded text-sm transition-opacity"
                      disabled={processing === file.name}
                    >
                      {processing === file.name ? '🔄 Processing...' : '🎬 Process'}
                    </button>
                  </div>
                ))}
              </div>
            </div>

            {/* Results */}
            <div className="bg-gray-700 p-4 rounded-lg">
              <h3 className="text-xl font-semibold mb-4 flex items-center">
                📊 Results ({files.results.length})
              </h3>
              <div className="max-h-96 overflow-y-auto space-y-2">
                {files.results.map((file, index) => (
                  <div key={index} className="flex items-center justify-between p-3 bg-gray-600 rounded group">
                    <div className="flex items-center gap-3 flex-1 min-w-0">
                      <span className="text-2xl">{getFileIcon(file)}</span>
                      <div className="flex-1 min-w-0">
                        <div className="font-mono text-sm truncate" title={file.path}>
                          {file.name}
                        </div>
                        <div className="text-xs text-gray-400 truncate" title={file.path}>
                          📁 {file.path}
                        </div>
                        <div className="text-xs text-gray-500">
                          📏 {formatFileSize(file.size)} • 🕒 {new Date(file.modified).toLocaleString()}
                        </div>
                      </div>
                    </div>
                    <button
                      onClick={() => handleProcessVideo(file)}
                      className="opacity-0 group-hover:opacity-100 bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded text-sm transition-opacity"
                      disabled={processing === file.name}
                    >
                      {processing === file.name ? '🔄 Processing...' : '🎯 Process'}
                    </button>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="mt-4 text-center text-gray-400 text-sm">
            Last updated: {new Date(files.timestamp).toLocaleString()}
          </div>
        </>
      )}

      {/* Coordinate Input Modal */}
      {showCoordinateModal && selectedFile && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-gray-800 p-6 rounded-lg shadow-xl max-w-md w-full mx-4">
            <h3 className="text-xl font-bold mb-4 text-white">
              🎯 SAM2 Processing Coordinates
            </h3>
            <p className="text-gray-400 mb-4">
              Processing: <span className="font-mono text-blue-400">{selectedFile.name}</span>
            </p>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  🏠 Nest Coordinates
                </label>
                <div className="grid grid-cols-2 gap-2">
                  <input
                    type="number"
                    value={coordinates.nestX}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, nestX: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="X"
                  />
                  <input
                    type="number"
                    value={coordinates.nestY}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, nestY: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="Y"
                  />
                </div>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  🐭 Mouse Coordinates
                </label>
                <div className="grid grid-cols-2 gap-2">
                  <input
                    type="number"
                    value={coordinates.mouseX}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, mouseX: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="X"
                  />
                  <input
                    type="number"
                    value={coordinates.mouseY}
                    onChange={(e) => setCoordinates(prev => ({ ...prev, mouseY: parseInt(e.target.value) || 0 }))}
                    className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600 focus:border-blue-500 focus:outline-none"
                    placeholder="Y"
                  />
                </div>
              </div>
            </div>
            
            <div className="flex gap-3 mt-6">
              <button
                onClick={() => setShowCoordinateModal(false)}
                className="flex-1 bg-gray-600 hover:bg-gray-700 text-white px-4 py-2 rounded transition-colors"
                disabled={!!processing}
              >
                Cancel
              </button>
              <button
                onClick={handleProcessConfirm}
                disabled={!!processing}
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded transition-colors disabled:opacity-50"
              >
                {processing ? '🔄 Processing...' : '🚀 Start Processing'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default NewLinuxFileBrowser;
