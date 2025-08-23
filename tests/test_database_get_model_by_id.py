from pathlib import Path
from datetime import datetime

from repositories import SqliteModelRepository
from models import Model

def test_get_model_by_id_returns_model(tmp_path):
    """Test that get_model_by_id returns the correct model when it exists in the database.
    
    :param tmp_path: Pytest temporary directory fixture
    :type tmp_path: Path
    """
    repo = SqliteModelRepository(str(tmp_path / "test.db"))
    model = Model(
        name="Test Model",
        parameters=7.9,
        max_context=2048,
        file_path=Path("/tmp/test.gguf"),
        file_size=12345,
        created_on=datetime.now().isoformat()
    )
    repo.add_model(model)

    fetched = repo.get_model_by_id(1)
    assert fetched is not None
    assert fetched.name == "Test Model"

def test_get_model_by_id_missing_returns_none(tmp_path):
    """Test that get_model_by_id returns None when the requested model ID doesn't exist.
    
    :param tmp_path: Pytest temporary directory fixture
    :type tmp_path: Path
    """    
    repo = SqliteModelRepository(str(tmp_path / "test.db"))
    assert repo.get_model_by_id(99) is None