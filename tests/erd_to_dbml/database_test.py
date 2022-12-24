from konstantin_docs.erd.erd import Relation
from konstantin_docs.erd_to_dbml.database import database_to_dbml

from konstantin_docs.erd import Column, Database, ProjectDefinition, Table


def test_empty():
    db = Database(tables=[])
    dbml: str = """

"""
    assert database_to_dbml(db) == dbml


def test_tables():
    db = Database(
        project_definition=ProjectDefinition("test_project"),
        tables=[
            Table(
                "table1",
                columns=[
                    table1_id := Column("id", "integer"),
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
    dbml = """
Project test_project {
    database_type: 'PostgreSQL'
    
}

Table table1 {
    id "integer" [null]

}

Table table2 {
    id "integer" [null]

}

Ref: table1.id > table2.id []

Ref: table1.id < table2.id []
"""  # noqa: W293
    assert database_to_dbml(db) == dbml
