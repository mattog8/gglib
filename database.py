"""Database operations."""

import sqlite3
from pathlib import Path

from models import Model

class Database:
    """SQLite database for model storage."""
    def __init__(self, db_path: str = 'models.db'):
        """Initialise SQLite database.
        
        :param db_path: Path to the SQLite database file
        :type db_path: str
        """
        self.db_path = db_path
        self.db_init()

    def db_init(self):
        """Create models table in SQLite database if it doesn't already exist."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS models (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    parameters REAL NOT NULL,
                    max_context INTEGER NOT NULL,
                    file_path TEXT UNIQUE NOT NULL,
                    file_size INTEGER NOT NULL,
                    created_on TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_model(self, model: Model) -> bool:
        """Add a model to the database.
        
        :param model: Model object to store
        :type model: Model

        :returns: True if commit to database successful
        :rtype: bool
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""INSERT INTO models (
                            name,
                            parameters, 
                            max_context,
                            file_path,
                            file_size,
                            created_on
                         ) VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    model.name,
                    model.parameters,
                    model.max_context,
                    str(model.file_path),
                    model.file_size,
                    model.created_on
                ))
            conn.commit()
            return True
        
    def get_model_by_id(self, model_id: int) -> Model | None:
        """Return a Model object for the given ID.

        :param model_id: The unique ID of the Model in the SQLite database.
        :type model_id: int

        :returns: The Model object if found, otherwise None.
        :rtype: Model | None
        """
        with sqlite3.connect(self.db_path) as conn: 
            cursor = conn.execute(
                """SELECT id, name, parameters, max_context, file_path, file_size, created_on
                    FROM models WHERE id = ?""", (model_id,)
             )
            row = cursor.fetchone()
            if row: 
                return Model(
                    name=row[1],
                    parameters=row[2],
                    max_context=row[3],
                    file_path=Path(row[4]),
                    file_size=row[5],
                    created_on=row[6]
                )
            return None
        
    def list(self) -> list[Model]:
        """Get all models from the database.

        :returns: List of all Model objects in the database. Returns empty list if no models found.
        :rtype: list[Model]

        .. note::
            Models are returned in the order they appear in the database.
    """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""SELECT
                                  id,
                                  name,
                                  parameters,
                                  max_context,
                                  file_path,
                                  file_size,
                                  created_on
                                  FROM models
                                  """)
            models = []
            for row in cursor:
                models.append(Model(
                    name=row[1],
                    parameters=row[2], 
                    max_context=row[3],
                    file_path=Path(row[4]),
                    file_size=row[5],
                    created_on=row[6]
                ))
            return models