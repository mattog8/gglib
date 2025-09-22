import { Model } from '@/types/api';

interface ModelCardProps {
    model: Model;
}

export default function ModelCard({ model }: ModelCardProps) {
  return (
    <div className="border p-4 rounded">
      <h3 className="font-bold">{model.name}</h3>
      <p>Parameters: {model.parameters}B</p>
      <p>Context: {model.max_context}</p>
      <p>Size: {model.file_size} bytes</p>
    </div>
  );
}