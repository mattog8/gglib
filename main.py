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
    pass