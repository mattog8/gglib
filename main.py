"""gglib - GGUF model manager and runner.
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
        console.print(f"[red]Not a File {file_path}[/red]")
        return False
    
    if not file_path.is_file():
        console.print(f"[red]Not a file: {file_path}[/red]")
        return False
    
    if file_path.suffix.lower() != '.gguf':
        console.print(f"[red]This application only support GGUF files and the .gguf extension was not detected: {file_path}[/red]")
        return False
    return True

@app.command()
def add(file_path: Path = typer.Argument(..., help = "Path to GGUF file to add.")):
    """Validates and collects metadata of a GGUF filepath.
    
    Args:
        file_path: Path to the GGUF file to validate and add

    Note:
        After validation, prompts user for model details including:
        - Model name
        
    """
    if not validate_gguf_file(file_path):
        return
    model_name = typer.prompt("Model name")
    console.print(f"[green] Valid GGUF file: {file_path.name}[/green]")

if __name__ == "__main__":
    app()