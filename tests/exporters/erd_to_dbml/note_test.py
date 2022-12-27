from dataclass_to_diagram.exporters.erd_to_dbml.note import note_to_dbml
from dataclass_to_diagram.models.erd import Note

import pytest

note_content = "note content"
note = Note(note_content)

LONG: str = """Note {{
   '''{content}'''
}}
"""

SHORT: str = "Note: '''{content}'''"

COLUMN: str = "note: '''{content}'''"


def test_view_default():
    assert note_to_dbml(note) == SHORT.format(content=note_content)


def test_view_long():
    assert note_to_dbml(note, "long") == LONG.format(content=note_content)


def test_view_short():
    assert note_to_dbml(note, "short") == SHORT.format(content=note_content)


def test_view_column():
    assert note_to_dbml(note, "column") == COLUMN.format(content=note_content)


def test_view_unknown():
    with pytest.raises(ValueError):
        note_to_dbml(note, "error")  # type: ignore
