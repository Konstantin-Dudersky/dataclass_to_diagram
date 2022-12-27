from dataclass_to_diagram.models.erd import Note
from dataclass_to_diagram.exporters.erd_to_dbml.enum import (
    Enum,
    EnumValue,
    enum_to_dbml,
)


def test_enum():
    enum = Enum(
        "my_enum",
        [
            EnumValue("value1"),
            EnumValue("value2", Note("note")),
        ],
    )
    dbml: str = """enum "my_enum" {
    value1
    value2 [note: '''note''']
}
"""
    assert enum_to_dbml(enum) == dbml
