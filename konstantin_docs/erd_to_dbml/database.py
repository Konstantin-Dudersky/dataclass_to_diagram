"""Преобразование всей схемы БД."""

from typing import Final

from konstantin_docs.erd import Database

from .project_definition import project_definition_to_dbml
from .relation import relation_to_dbml
from .table import table_to_dbml

TEMPLATE: Final[
    str
] = """
{project_definition}{tables}{relations}
"""


def database_to_dbml(database: Database) -> str:
    """Преобразование всей схемы БД."""
    if database.project_definition:
        proj_def = "{0}\n".format(
            project_definition_to_dbml(database.project_definition),
        )
    else:
        proj_def = ""
    tables: list[str] = [table_to_dbml(table) for table in database.tables]
    if database.relations is not None:
        relations_list: list[str] = [
            relation_to_dbml(rel) for rel in database.relations
        ]
        relations_str = "\n\n".join(relations_list)
        relations = "\n{0}".format(relations_str)
    else:
        relations = ""
    return TEMPLATE.format(
        project_definition=proj_def,
        tables="\n".join(tables),
        relations=relations,
    )
