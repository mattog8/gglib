from abc import ABC, abstractmethod
from typing import List
import sqlite3
from pathlib import Path
from models import Model

class ModelRepository(ABC):
    """Abstract repository defining the contract for model storage."""
    
    @abstractmethod
    def add_model(self, model: Model) -> bool:
        """Add a model to storage."""
        pass
    
    @abstractmethod 
    def get_model_by_id(self, model_id: int) -> Model | None:
        """Get a model by its ID."""
        pass
    
    @abstractmethod
    def list(self) -> list[Model]:
        """Get all models from storage."""
        pass

class SqliteModelRepository(ModelRepository):
    """SQLite implementation of ModelRepository."""
    
    def __init__(self, db_path: str = 'models.db'):
        """Initialise SQLite database"""
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Create models table - copied from Database.db_init"""
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
        """Add a model."""
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
        """Get model by ID."""
        with sqlite3.connect(self.db_path) as conn: 
            cursor = conn.execute(
                """SELECT id, name, parameters, max_context, file_path, file_size, created_on
                    FROM models WHERE id = ?""", (model_id,)
             )
            row = cursor.fetchone()
            if row: 
                return Model(
                    id=row[0],
                    name=row[1],
                    parameters=row[2],
                    max_context=row[3],
                    file_path=Path(row[4]),
                    file_size=row[5],
                    created_on=row[6]
                )
            return None

    def list(self) -> list[Model]:
        """Get all models."""
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
                    id=row[0],
                    name=row[1],
                    parameters=row[2], 
                    max_context=row[3],
                    file_path=Path(row[4]),
                    file_size=row[5],
                    created_on=row[6]
                ))
            return models
        
