from dataclass_to_diagram.exporters.erd_to_dbml.table import (
    Table,
    table_to_dbml,
)

from dataclass_to_diagram.models.erd import Column, Note


def test_empty():
    table = Table("table_name", [])
    dbml = """Table table_name {


}
"""
    assert table_to_dbml(table) == dbml


def test_columns():
    table = Table(
        name="table_name",
        columns=[
            Column("id", "integer"),
        ],
    )
    dbml = """Table table_name {
    id "integer" [null]

}
"""
    assert table_to_dbml(table) == dbml


def test_note():
    note_content: str = """note
content"""
    table = Table(
        name="table_name",
        columns=[],
        note=Note(note_content),
    )
    dbml = """Table table_name {

    Note: '''note
content'''
}
"""
    assert table_to_dbml(table) == dbml


def test_all_fields():
    note_content: str = """note
content"""
    table = Table(
        name="table_name",
        columns=[
            Column("id", "integer", is_pk=True),
            Column("desc", "varchar"),
        ],
        note=Note(note_content),
    )
    dbml = """Table table_name {
    id "integer" [pk, null]
    desc "varchar" [null]
    Note: '''note
content'''
}
"""
    assert table_to_dbml(table) == dbml
