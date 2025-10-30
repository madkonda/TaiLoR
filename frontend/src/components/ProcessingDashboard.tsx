import React, { useState, useEffect } from 'react';
import { apiUrl } from '../config';

interface ProcessingStep {
  name: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  message: string;
  progress: number;
}

interface ProcessingJob {
  id: string;
  filename: string;
  nestCoords: [number, number];
  mouseCoords: [number, number];
  status: 'pending' | 'processing' | 'completed' | 'failed';
  progress: number;
  steps: ProcessingStep[];
}

const ProcessingDashboard: React.FC = () => {
  const [jobs, setJobs] = useState<ProcessingJob[]>([]);
  const [isConnected, setIsConnected] = useState(false);

  // Poll for job updates every 2 seconds
  useEffect(() => {
    const fetchJobs = async () => {
      try {
        // Use health for connectivity; jobs may not exist in prod
        const response = await fetch(apiUrl('/health'));
        if (response.ok) {
          setJobs([]);
          setIsConnected(true);
        } else {
          setIsConnected(false);
        }
      } catch (error) {
        console.error('Error fetching jobs:', error);
        setIsConnected(false);
      }
    };

    // Fetch jobs immediately
    fetchJobs();
    
    // Set up polling
    const interval = setInterval(fetchJobs, 2000);
    
    return () => clearInterval(interval);
  }, []);

  const getStepIcon = (step: ProcessingStep) => {
    switch (step.status) {
      case 'completed':
        return '✅';
      case 'failed':
        return '❌';
      case 'processing':
        return '🔄';
      default:
        return '⏳';
    }
  };

  return (
    <div className="processing-dashboard p-6 bg-gray-800 rounded-lg shadow-lg text-white">
      <h2 className="text-3xl font-bold mb-6 text-center">Real-time Processing Dashboard</h2>
      <div className="flex items-center justify-center mb-6">
        <span className={`inline-block w-4 h-4 rounded-full mr-2 ${isConnected ? 'bg-green-500' : 'bg-red-500'}`}></span>
        <span className="text-lg">{isConnected ? 'Connected to Backend' : 'Disconnected from Backend'}</span>
      </div>

      {jobs.length === 0 ? (
        <p className="text-center text-gray-400">No active processing jobs. Upload a video to start!</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {jobs.map((job) => (
            <div key={job.id} className="job-card bg-gray-700 p-5 rounded-lg shadow-md">
              <h3 className="text-xl font-semibold mb-3 flex items-center">
                {job.status === 'completed' ? '🎉' : job.status === 'failed' ? '🚨' : '⚙️'} {job.filename}
              </h3>
              <p className="text-sm text-gray-400 mb-2">Job ID: {job.id}</p>
              <p className="text-sm text-gray-400 mb-2">Nest: {job.nestCoords?.join(', ')} | Mouse: {job.mouseCoords?.join(', ')}</p>
              
              {/* Overall Progress Bar */}
              <div className="w-full bg-gray-600 rounded-full h-2.5 mb-4">
                <div 
                  className={`h-2.5 rounded-full ${job.status === 'completed' ? 'bg-green-500' : job.status === 'failed' ? 'bg-red-500' : 'bg-blue-500'}`} 
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
                      <p className="font-medium">{step.message}</p>
                      <div className="w-full bg-gray-600 rounded-full h-1.5">
                        <div 
                          className={`h-1.5 rounded-full ${step.status === 'completed' ? 'bg-green-400' : step.status === 'failed' ? 'bg-red-400' : 'bg-blue-400'}`} 
                          style={{ width: `${step.progress}%` }}
                        ></div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ProcessingDashboard;