from typing import Final

from konstantin_docs.erd import Column

from .note import note_to_dbml

TEMPLATE: Final[str] = "{name} {datatype} [{settings}]"


def column_to_dbml(column: Column) -> str:
    settings: list[str] = []
    if column.note:
        settings.append(note_to_dbml(column.note, "column"))
    if column.is_pk:
        settings.append("pk")
    if column.can_be_null:
        settings.append("null")
    else:
        settings.append("not null")
    if column.is_unique:
        settings.append("unique")
    if column.default_value is not None:
        settings.append("default: '{0}'".format(column.default_value))
    if column.is_increment:
        settings.append("increment")

    return TEMPLATE.format(
        name=column.name,
        datatype='"{0}"'.format(column.datatype),
        settings=", ".join(settings),
    )
