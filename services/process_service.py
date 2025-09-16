"""Process management for GGUF model server execution."""

from pathlib import Path
import subprocess

class ProcessService:
    """Manage llama-server and llama-cli process execution."""

    def __init__(self, cpp_server_command: str = 'llama-server', cpp_cli_command: str = 'llama-cli'):
        """Initialise ProcessService.
        
        :param cpp_server_command: Path to llama-server executable or alias.
        :type cpp_server_command: str
        :param cpp_cli_command: Path to llama-cli executable or alias.
        :type cpp_cli_command: str
        """
        self.server_command = cpp_server_command
        self.cli_command = cpp_cli_command

    def _run_llama_command(self, command: str, model_path: Path, ctx_len: int | None = None) -> subprocess.CompletedProcess:
        """Generic method to run llama commands with common parameters.
        
        :param command: The llama command to run (e.g., 'llama-server', 'llama-cli')
        :type command: str
        :param model_path: Path to the GGUF model file
        :type model_path: Path
        :param ctx_len: Context length `-c` pass to command. None by default unless specified.
        :type ctx_len: int | None
        :returns: Completed process information
        :rtype: CompletedProcess
        """
        cmd = [command, '-m', str(model_path)]

        if ctx_len:
            cmd.extend(['-c', str(ctx_len)])

        return subprocess.run(cmd)

    def start_server(self, model_path: Path, ctx_len: int | None = None) -> subprocess.CompletedProcess:
        """Start llama-server with the specified model and, optionally, a given context length.
        
        :param model_path: Path to the GGUF model file
        :type model_path: Path
        :param ctx_len: Context length `-c` pass to `llama-server`. None by default unless specified.
        :type ctx_len: int | None
        :returns: Completed process information
        :rtype: CompletedProcess
        """
        return self._run_llama_command(self.server_command, model_path, ctx_len)

    def start_cli(self, model_path: Path, ctx_len: int | None = None) -> subprocess.CompletedProcess:
        """Start llama-cli with the specified model and, optionally, a given context length.
        
        :param model_path: Path to the GGUF model file
        :type model_path: Path
        :param ctx_len: Context length `-c` pass to `llama-cli`. None by default unless specified.
        :type ctx_len: int | None
        :returns: Completed process information
        :rtype: CompletedProcess
        """
        return self._run_llama_command(self.cli_command, model_path, ctx_len)