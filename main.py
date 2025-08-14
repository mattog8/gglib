"""
gglib - GGUF model manager and runner.
"""

import typer

app = typer.Typer(
    name="gglib",
    help="Manage and run local GGUF models",
    no_args_is_help=True
)

