"""GGUF file data models."""

from dataclasses import dataclass
from pathlib import Path
from datetime import datetime

@dataclass
class Model: 
    """Represents a GGUF model with collected metadata."""
    name: str
    parameters: float
    max_context: int
    file_path: Path
    file_size: int
    created_on: str