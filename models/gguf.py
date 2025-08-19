"""GGUF file data models."""

from dataclasses import dataclass
from pathlib import Path
from datetime import datetime

@dataclass
class Model: 
    """Represent a GGUF model with metadata collected during registration.
    
    This dataclass stores essential information about a GGUF (GPT-Generated Unified Format)
    model file, including its configuration parameters and filesystem details.
    
    :param name: Human-readable name/identifier for the model
    :type name: str
    :param parameters: Number of parameters in the model (e.g., 7.0 for 7B parameters)  
    :type parameters: float
    :param max_context: Maximum context window size the model supports
    :type max_context: int
    :param file_path: Absolute path to the .gguf model file
    :type file_path: Path
    :param file_size: Size of the model file in bytes
    :type file_size: int
    :param created_on: ISO format timestamp when the model was added to the registry
    :type created_on: str
        
    Example::     
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
    id: int = None