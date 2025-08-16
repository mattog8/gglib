from pathlib import Path
from datetime import datetime

from database import Database
from models import Model

def test_get_model_by_id_returns_model(tmp_path):
    db = Database(str(tmp_path / "test.db"))
    model = Model(
        name="Test Model",
        parameters=7.9,
        max_context=2048,
        file_path=Path("/tmp/test.gguf"),
        file_size=12345,
        created_on=datetime.now().isoformat()
    )
    db.add_model(model)

    fetched = db.get_model_by_id(1)
    assert fetched is not None
    assert fetched.name == "Test Model"

def test_get_model_by_id_missing_returns_none(tmp_path):
    db = Database(str(tmp_path / "test.db"))
    assert db.get_model_by_id(99) is None