from dataclass_to_diagram.models.erd import (
    Database,
    Column,
    Enum,
    EnumValue,
    ProjectDefinition,
    Relation,
    Table,
)

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
