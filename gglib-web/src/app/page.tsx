'use client';

import { useEffect, useState } from 'react';
import ModelCard from '@/components/ModelCard';
import { Model } from '@/types/api';
import { ApiClient } from '@/services/api';

export default function Home() {
  const [models, setModels] = useState<Model[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchModels() {
      try {
        const modelData = await ApiClient.getModels();
        setModels(modelData);
      } catch (err) {
        setError('Failed to load models');
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    fetchModels();
  }, []);

  if (loading) return <div className="p-8">Loading models...</div>;
  if (error) return <div className="p-8 text-red-500">{error}</div>;

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">GGLIB Model Manager</h1>
      {models.length === 0 ? (
        <p>No models found. Add some models using the CLI first!</p>
      ) : (
        <div className="grid gap-4">
          {models.map((model) => (
            <ModelCard key={model.id} model={model} />
          ))}
        </div>
      )}
    </div>
  );
}