"""Database operations."""

import sqlite3

class Database:
    """SQLite database for model storage."""
    def __init__(self, db_path: str = 'models.db'):
        """Initialise SQLite database.
        
        Args:
        db_path: Path to the SQLite database file
        """
        self.db_path = db_path