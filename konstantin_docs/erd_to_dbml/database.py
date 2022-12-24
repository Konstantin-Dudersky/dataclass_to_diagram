"""Преобразование всей схемы БД."""

# pyright: reportShadowedImports=false

from typing import Final, Iterable

from konstantin_docs.erd import (
    Database,
    Enum,
    ProjectDefinition,
    Relation,
    Table,
)

from .enum import enum_to_dbml
from .project_definition import project_definition_to_dbml
from .relation import relation_to_dbml
from .table import table_to_dbml

TEMPLATE: Final[
    str
] = """
{project_definition}{enums}{tables}{relations}
"""


def _proj_def_to_dbml(proj_def: ProjectDefinition | None) -> str:
    if proj_def is None:
        return ""
    return "{0}".format(project_definition_to_dbml(proj_def))


def _enums_to_dbml(enums: Iterable[Enum] | None) -> str:
    if enums is None:
        return ""
    enums_list: list[str] = [enum_to_dbml(enum) for enum in enums]
    enums_str = "\n".join(enums_list)
    return "\n{0}".format(enums_str)


def _tables_to_dbml(tables: Iterable[Table] | None) -> str:
    if tables is None:
        return ""
    tables_list: list[str] = [table_to_dbml(table) for table in tables]
    tables_str = "\n".join(tables_list)
    return "\n{0}".format(tables_str)


def _relations_to_dbml(relations: Iterable[Relation] | None) -> str:
    if relations is None:
        return ""
    relations_list: list[str] = [relation_to_dbml(rel) for rel in relations]
    relations_str = "\n\n".join(relations_list)
    return "\n{0}".format(relations_str)


def database_to_dbml(database: Database) -> str:
    """Преобразование всей схемы БД."""
    return TEMPLATE.format(
        project_definition=_proj_def_to_dbml(database.project_definition),
        enums=_enums_to_dbml(database.enums),
        tables=_tables_to_dbml(database.tables),
        relations=_relations_to_dbml(database.relations),
    )
