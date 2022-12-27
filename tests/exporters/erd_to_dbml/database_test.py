from dataclass_to_diagram.models.erd import Relation
from dataclass_to_diagram.exporters.erd_to_dbml.database import database_to_dbml

from dataclass_to_diagram.models.erd import (
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
    """Тестирование полной конфигурации.

    Отлаживать после работы остальных тестов.
    """
    db = Database(
        project_definition=ProjectDefinition("test_project"),
        enums=[
            user_status := Enum(
                "user_status",
                [
                    EnumValue("active"),
                    EnumValue("inactive"),
                ],
            ),
        ],
        tables=[
            Table(
                "user",
                columns=[
                    user_id := Column("id", "integer"),
                    Column("status", user_status),
                ],
                table_group="users",
            ),
            Table(
                "table2",
                columns=[
                    table2_id := Column("id", "integer"),
                ],
            ),
        ],
        relations=[
            Relation(user_id, ">", table2_id),
            Relation(user_id, "<", table2_id),
        ],
    )
    dbml: str = """
Project test_project {
    database_type: 'PostgreSQL'
    
}

enum "user_status" {
    active
    inactive
}

Table user {
    id "integer" [null]
    status "user_status" [null]

}

Table table2 {
    id "integer" [null]

}

Ref: user.id > table2.id []

Ref: user.id < table2.id []

TableGroup users {
    user
}

"""  # noqa: W293
    assert database_to_dbml(db) == dbml
