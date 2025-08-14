"""
gglib - GGUF model manager and runner.
"""

import typer
from pathlib import Path
from rich.console import Console

app = typer.Typer(
    name="gglib",
    help="Manage and run local GGUF models",
    no_args_is_help=True
)

console = Console()

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
    if not file_path.exists():
        console.print(f"[red]Note a File {file_path}[/red]")
        return False
    
    if not file_path.is_file():
        console.print(f"[red]Not a file: {file_path}[/red]")
        return False
    
    if file_path.suffix.lower() != '.gguf':
        console.print(f"[red]This application only support GGUF files and the .gguf extension was not detected: {file_path}[/red]")
        return False
    return True