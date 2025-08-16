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

    def start_server(self, model_path: Path) -> subprocess.CompletedProcess:
        """Start llama-server with the specified model.
        
        :param model_path: Path to the GGUF model file
        :type model_path: Path
        :returns: Completed process information
        :rtype: CompletedProcess
        """
        cmd = [self.server_command, '-m', model_path]
        return subprocess.run(cmd)