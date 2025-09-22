export interface Model {
    name: string;
    parameters: number;
    max_context: number;
    file_path: string;
    file_size: number;
    created_on: string;
    id?: number | null;
} 