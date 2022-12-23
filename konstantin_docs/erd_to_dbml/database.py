"""Преобразование всей схемы БД."""

from typing import Final

from konstantin_docs.erd import Database

from .project_definition import project_definition_to_dbml
from .table import table_to_dbml

TEMPLATE: Final[
    str
] = """
{project_definition}
{tables}
"""


def database_to_dbml(database: Database) -> str:
    """Преобразование всей схемы БД."""
    if database.project_definition:
        proj_def = project_definition_to_dbml(database.project_definition)
    else:
        proj_def = ""
    tables: list[str] = [table_to_dbml(table) for table in database.tables]

    return TEMPLATE.format(
        project_definition=proj_def,
        tables="\n\n".join(tables),
    )
