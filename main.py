"""gglib - GGUF model manager and runner."""

import typer
from pathlib import Path
from rich.console import Console
from datetime import datetime

from models import Model
from database import Database

app = typer.Typer(
    name="gglib",
    help="Manage and run local GGUF models",
    no_args_is_help=True
)

console = Console()
db = Database()

def validate_gguf_file(file_path: Path) -> bool:
    """Validate a given file and verify that it confirms to the criteria.

    :param file_path: Path to the GGUF file to validate
    :type file_path: Path

    :returns: True if file meets criteria, False otherwise
    :rtype: bool

    .. note::
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
    """Validate and collect metadata of a GGUF filepath then add it to the SQLite database.
    
    :param file_path: Path to the GGUF file to validate and add to database
    :type file_path: Path

    .. note::
        After validation, prompts user for model details including:
        - Model name
        - Parameters
        - Context length
        
    """
    if not validate_gguf_file(file_path):
        return
    
    model_name = typer.prompt("Model name")
    model_params = typer.prompt("Parameters")
    model_max_ctx = typer.prompt("Maximum context size")

    model = Model(
        name=model_name,
        parameters=model_params, 
        max_context=model_max_ctx,
        file_path=file_path,
        file_size=file_path.stat().st_size,
        created_on=datetime.now().isoformat()
    )

    db.add_model(model)

    console.print(f"[purple]{model.name}[/purple] [green]has been added.[/green]")

if __name__ == "__main__":
    app()