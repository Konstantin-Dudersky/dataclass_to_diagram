from konstantin_docs.erd.erd import Relation
from konstantin_docs.erd_to_dbml.database import database_to_dbml

from konstantin_docs.erd import (
    Column,
    Database,
    Enum,
    EnumValue,
    ProjectDefinition,
    Table,
)


def test_empty():
    db = Database()
    dbml: str = """

"""
    assert database_to_dbml(db) == dbml


def test_database():
    db = Database(
        project_definition=ProjectDefinition("test_project"),
        enums=[
            test_enum := Enum(
                "test_enum",
                [
                    EnumValue("enum_value_1"),
                    EnumValue("enum_value_2"),
                ],
            ),
        ],
        tables=[
            Table(
                "table1",
                columns=[
                    table1_id := Column("id", "integer"),
                    Column("state", test_enum),
                ],
            ),
            Table(
                "table2",
                columns=[
                    table2_id := Column("id", "integer"),
                ],
            ),
        ],
        relations=[
            Relation(table1_id, ">", table2_id),
            Relation(table1_id, "<", table2_id),
        ],
    )
    dbml: str = """
Project test_project {
    database_type: 'PostgreSQL'
    
}

enum "test_enum" {
    enum_value_1
    enum_value_2
}

Table table1 {
    id "integer" [null]
    state "test_enum" [null]

}

Table table2 {
    id "integer" [null]

}

Ref: table1.id > table2.id []

Ref: table1.id < table2.id []
"""  # noqa: W293
    assert database_to_dbml(db) == dbml
