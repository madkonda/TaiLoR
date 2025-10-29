import React, { useState, useEffect } from 'react';
import { io } from 'socket.io-client';

interface ProcessingStep {
  name: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  message: string;
  completedAt?: string;
}

interface ProcessingJob {
  id: string;
  filename: string;
  nestCoords: [number, number];
  mouseCoords: [number, number];
  status: 'uploading' | 'processing' | 'completed' | 'failed';
  progress: number;
  currentStep: string;
  startTime: string;
  lastUpdated: string;
  steps: ProcessingStep[];
}

const ProcessingDashboard: React.FC = () => {
  const [jobs, setJobs] = useState<ProcessingJob[]>([]);
  const [socket, setSocket] = useState<any>(null);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    // Connect to WebSocket server - always use localhost for now
    const websocketUrl = 'http://localhost:3002';
    const newSocket = io(websocketUrl);
    setSocket(newSocket);

    newSocket.on('connect', () => {
      console.log('Connected to WebSocket server');
      setIsConnected(true);
    });

    newSocket.on('disconnect', () => {
      console.log('Disconnected from WebSocket server');
      setIsConnected(false);
    });

    newSocket.on('current_jobs', (currentJobs: ProcessingJob[]) => {
      setJobs(currentJobs);
    });

    newSocket.on('job_created', (job: ProcessingJob) => {
      setJobs(prev => [...prev, job]);
    });

    newSocket.on('job_update', (updatedJob: ProcessingJob) => {
      setJobs(prev => prev.map(job => 
        job.id === updatedJob.id ? updatedJob : job
      ));
    });

    newSocket.on('job_deleted', (jobId: string) => {
      setJobs(prev => prev.filter(job => job.id !== jobId));
    });

    return () => {
      if (socket) {
        socket.close();
      }
    };
  }, []);

  const getStepIcon = (step: ProcessingStep) => {
    switch (step.status) {
      case 'completed':
        return '✅';
      case 'processing':
        return '🔄';
      case 'failed':
        return '❌';
      default:
        return '⏳';
    }
  };

  const getStepColor = (step: ProcessingStep) => {
    switch (step.status) {
      case 'completed':
        return 'text-green-600';
      case 'processing':
        return 'text-blue-600';
      case 'failed':
        return 'text-red-600';
      default:
        return 'text-gray-500';
    }
  };

  const formatTime = (timeString: string) => {
    return new Date(timeString).toLocaleTimeString();
  };

  const getDuration = (startTime: string, endTime?: string) => {
    const start = new Date(startTime);
    const end = endTime ? new Date(endTime) : new Date();
    const diff = end.getTime() - start.getTime();
    const minutes = Math.floor(diff / 60000);
    const seconds = Math.floor((diff % 60000) / 1000);
    return `${minutes}m ${seconds}s`;
  };

  return (
    <div className="processing-dashboard">
      <div className="dashboard-header">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">
          🎬 Video Processing Dashboard
        </h2>
        <div className="flex items-center gap-4 mb-6">
          <div className={`flex items-center gap-2 px-3 py-1 rounded-full text-sm ${
            isConnected ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
          }`}>
            <div className={`w-2 h-2 rounded-full ${
              isConnected ? 'bg-green-500' : 'bg-red-500'
            }`}></div>
            {isConnected ? 'Connected' : 'Disconnected'}
          </div>
          <div className="text-sm text-gray-600">
            {jobs.length} job{jobs.length !== 1 ? 's' : ''} active
          </div>
        </div>
      </div>

      {jobs.length === 0 ? (
        <div className="text-center py-12">
          <div className="text-6xl mb-4">📹</div>
          <h3 className="text-xl font-semibold text-gray-600 mb-2">
            No videos being processed
          </h3>
          <p className="text-gray-500">
            Upload a video to see the processing pipeline in action!
          </p>
        </div>
      ) : (
        <div className="space-y-6">
          {jobs.map((job) => (
            <div key={job.id} className="bg-white rounded-lg shadow-lg border border-gray-200 overflow-hidden">
              <div className="p-6">
                <div className="flex items-center justify-between mb-4">
                  <div>
                    <h3 className="text-lg font-semibold text-gray-800">
                      {job.filename}
                    </h3>
                    <p className="text-sm text-gray-600">
                      Started: {formatTime(job.startTime)} • 
                      Duration: {getDuration(job.startTime)}
                    </p>
                  </div>
                  <div className="text-right">
                    <div className="text-2xl font-bold text-blue-600">
                      {job.progress}%
                    </div>
                    <div className="text-sm text-gray-600">
                      {job.currentStep}
                    </div>
                  </div>
                </div>

                {/* Progress Bar */}
                <div className="w-full bg-gray-200 rounded-full h-3 mb-6">
                  <div 
                    className="bg-gradient-to-r from-blue-500 to-green-500 h-3 rounded-full transition-all duration-500 ease-out"
                    style={{ width: `${job.progress}%` }}
                  ></div>
                </div>

                {/* Processing Steps */}
                <div className="space-y-3">
                  {job.steps.map((step) => (
                    <div key={step.name} className="flex items-center gap-3">
                      <div className="text-2xl">
                        {getStepIcon(step)}
                      </div>
                      <div className="flex-1">
                        <div className={`font-medium ${getStepColor(step)}`}>
                          {step.message}
                        </div>
                        {step.completedAt && (
                          <div className="text-xs text-gray-500">
                            Completed: {formatTime(step.completedAt)}
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </div>

                {/* Coordinates Display */}
                <div className="mt-4 pt-4 border-t border-gray-200">
                  <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                      <span className="font-medium text-gray-700">Nest Position:</span>
                      <span className="ml-2 text-gray-600">
                        ({job.nestCoords[0]}, {job.nestCoords[1]})
                      </span>
                    </div>
                    <div>
                      <span className="font-medium text-gray-700">Mouse Position:</span>
                      <span className="ml-2 text-gray-600">
                        ({job.mouseCoords[0]}, {job.mouseCoords[1]})
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ProcessingDashboard;
