import { Model } from '@/types/api';

// Base URL for your FastAPI backend
const API_BASE_URL = 'http://localhost:8000';

export class ApiClient {
  // Fetch all models from your FastAPI /api/models endpoint
  static async getModels(): Promise<Model[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/models`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      
      // Your FastAPI returns { models: [...] }
      return data.models;
    } catch (error) {
      console.error('Failed to fetch models:', error);
      throw error;
    }
  }
}