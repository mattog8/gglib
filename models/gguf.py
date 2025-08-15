"""GGUF file data models."""

from dataclasses import dataclass
from pathlib import Path
from datetime import datetime

@dataclass
class Model: 
    """Represents a GGUF model with metadata collected during registration.
    
    This dataclass stores essential information about a GGUF (GPT-Generated Unified Format)
    model file, including its configuration parameters and filesystem details.
    
    Attributes:
        name (str): Human-readable name/identifier for the model
        parameters (float): Number of parameters in the model (e.g., 7.0 for 7B parameters)
        max_context (int): Maximum context window size the model supports
        file_path (Path): Absolute path to the .gguf model file
        file_size (int): Size of the model file in bytes
        created_on (str): ISO format timestamp when the model was added to the registry
        
    Example:
        >>> model = Model(
        ...     name="Llama-2-7B-Chat",
        ...     parameters=7.0,
        ...     max_context=4096,
        ...     file_path=Path("/models/llama-2-7b-chat.gguf"),
        ...     file_size=13481000000,
        ...     created_on="2025-08-15T10:30:00"
        ... )
    """
    name: str
    parameters: float
    max_context: int
    file_path: Path
    file_size: int
    created_on: str