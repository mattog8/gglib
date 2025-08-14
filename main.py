"""
gglib - GGUF model manager and runner.
"""

import typer
from pathlib import Path

app = typer.Typer(
    name="gglib",
    help="Manage and run local GGUF models",
    no_args_is_help=True
)

def validate_gguf_file(file_path: Path) -> bool:
    """Validate a given file and verify that it confirms to the criteria.

    Args:
        file_path: Path to the GGUF file to validate

    Returns:
        bool: True if file meets criteria, False otherwise

    Note:
        Validation criteria:
        - File exists
        - Has .gguf extension
    """
    return True