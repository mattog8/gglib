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