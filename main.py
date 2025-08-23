"""gglib - GGUF model manager and runner."""

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from datetime import datetime
from typing import List

from models import Model
from repositories import SqliteModelRepository
from services import ProcessService

app = typer.Typer(
    name="gglib",
    help="Manage and run local GGUF models",
    no_args_is_help=True
)

console = Console()
model_repo = SqliteModelRepository()
process_service = ProcessService()

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
        id=None,
        name=model_name,
        parameters=model_params, 
        max_context=model_max_ctx,
        file_path=file_path,
        file_size=file_path.stat().st_size,
        created_on=datetime.now().isoformat()
    )

    model_repo.add_model(model)

    console.print(f"[purple]{model.name}[/purple] [green]has been added.[/green]")

@app.command()
def lib():
    """View the library: print models in the database.
    
    :param models: List of models to display
    :type models: list
    """
    models = model_repo.list()

    if not models: #show alert that no models were returned
        console.print("[yellow]No models found in database[/yellow]")
        return

    table = Table(title=f"Models ({len(models)}) found")
    table.add_column("ID")
    table.add_column("Name")

    for model in models: #add rows to the table
        table.add_row(
            str(model.id),
            model.name
        )
    console.print(table)

@app.command()
def serve(
        model_id: int = typer.Argument(
            ..., 
            help = "Model ID to serve."
        ),
        context: int | None = typer.Option(
            None, 
            '-c', 
            '--context',
            help="Specify a context length when serving a model"
        )
    ):
    """Serve a model by providing its database ID.
    
    :param model_id: Database ID of the model to serve
    :type model_id: int
    :param context: Context length flag for serve command. None by default
    :type context: int | None
    """
    model = model_repo.get_model_by_id(model_id)
    if not model: #Show an error if the model is not found
        console.print(f"[red]Model with ID {model_id} not found.[/red]")
        return
    console.print(f"[blue]Serving {model.name}...[/blue]")
    console.print(f"[yellow]Press Ctrl+C to stop the server[/yellow]")

    try:
        process_service.start_server(model.file_path, context)
    except KeyboardInterrupt:
        console.print(f"[blue]Server stopped[/blue]")

if __name__ == "__main__":
    app()