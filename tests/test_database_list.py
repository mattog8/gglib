"""Tests for Database.list() method."""

from pathlib import Path
from datetime import datetime

from database import Database
from models import Model

def test_list_empty_returns_empty_list(tmp_path):
    """Empty database returns an empty list."""
    db = Database(str(tmp_path / "models.db"))
    result = db.list()
    assert result == []
    assert isinstance(result, list)

def test_list_single_model_returns_model(tmp_path):
    """Single inserted model is returned with matching fields."""
    db = Database(str(tmp_path / "models.db"))
    model = Model(
        name="Test Model",
        parameters=7.0,
        max_context=2048,
        file_path=Path("/tmp/test.gguf"),
        file_size=1234,
        created_on=datetime.now().isoformat()
    )

    db.add_model(model)
    result = db.list()
    assert len(result) == 1
    m = result[0]
    assert m.name == "Test Model"
    assert m.parameters == 7.0
    assert m.max_context == 2048
    assert m.file_path == Path("/tmp/test.gguf")
    assert m.file_size == 1234
    assert m.id is not None

def test_list_multiple_models_returns_models(tmp_path):
    """Multiple models are inserted and returned with matching fields."""
    db = Database(str(tmp_path / "models.db"))
    model_data = { #Dictionary holding test model metadata (3 models).
        "name": 
            [f"Test Model {x}" for x in range(1,4)],
        "parameters": 
            [7.2, 32.5, 70.5],
        "max_context": 
            [2048, 131072, 32768],
        "file_path":
            [Path(f"/tmp/test{x}.gguf") for x in range(1,4)],
        "file_size":
            [1234, 9876, 5555],
        "created_on": 
            [datetime.now().isoformat() for _ in range (1,4)]
        }
    
    for i in range(3): #Loop to instantiate test models.
        model = Model(
            name=model_data["name"][i],
            parameters=model_data["parameters"][i],
            max_context=model_data["max_context"][i],
            file_path=model_data["file_path"][i],
            file_size=model_data["file_size"][i],
            created_on=model_data["created_on"][i]
        )
        db.add_model(model)

    result = db.list()
    assert len(result) == 3

    for i, model in enumerate(result): #Loop through enumeration of list return.
        assert model.name == model_data["name"][i]
        assert model.parameters == model_data["parameters"][i]
        assert model.max_context == model_data["max_context"][i]
        assert model.file_path == model_data["file_path"][i]
        assert model.file_size == model_data["file_size"][i]
        assert model.created_on == model_data["created_on"][i]
        assert model.id is not None

