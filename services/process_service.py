"""Process management for GGUF model server execution."""

from pathlib import Path
import subprocess

class ProcessService:
    """Manage llama-server process execution."""

    def __init__(self, cpp_server_command: str = 'llama-server'):
        """Initialise ProcessService.
        
        :param cpp_server_command: Path to llama-server executable or alias.
        :type cpp_server_command: str
        """
        self.server_command = cpp_server_command

    def start_server(self, model_path: Path, ctx_len: int | None = None) -> subprocess.CompletedProcess:
        """Start llama-server with the specified model and, optionally, a given context length.
        
        :param model_path: Path to the GGUF model file
        :type model_path: Path
        :param ctx_len: Context length `-c` pass to `llama-server`. None by unless specified.
        :type ctx_len: int | None
        :returns: Completed process information
        :rtype: CompletedProcess
        """
        cmd = [self.server_command, '-m', str(model_path)]

        if ctx_len: #If passed the optional ctx_len parameter, extend command list 
            cmd.extend(['-c', str(ctx_len)])

        return subprocess.run(cmd)