"""Датаклассы для определения схемы БД."""

from dataclasses import dataclass, field
from typing import Iterable, Literal, TypeAlias

REL_TYPES: TypeAlias = Literal["<", ">", "-", "<>"]
REL_CONFIG: TypeAlias = Literal[
    "cascade",
    "restrict",
    "set null",
    "set default",
    "no action",
]


@dataclass
class Note(object):
    """Описание элемента."""

    note_content: str


@dataclass
class ProjectDefinition(object):
    """Description of the project."""

    project_name: str
    database_type: str = "PostgreSQL"
    note: Note | None = None


@dataclass
class EnumValue(object):
    """Одно значение в перечислении."""

    enum_value: str
    note: Note | None = None


@dataclass
class Enum(object):
    """Перечисление."""

    name: str
    enum_values: Iterable[EnumValue]


DATATYPES: TypeAlias = (
    Enum
    | Literal[
        "integer",
        "varchar",
    ]
)


@dataclass
class Column(object):
    """Столбец в БД."""

    name: str
    datatype: DATATYPES
    note: None | Note = None
    is_pk: bool = False
    can_be_null: bool = True
    is_unique: bool = False
    is_increment: bool = False
    default_value: str | None = None
    table: "Table" = field(default=None, init=False)  # type: ignore


@dataclass
class Table(object):
    """Таблица."""

    name: str
    columns: Iterable[Column]
    note: Note | None = None

    def __post_init__(self) -> None:
        """Задать ссылки из столбцов на таблицу."""
        for column in self.columns:
            column.table = self


@dataclass
class Relation(object):
    """Связи между таблицами."""

    column1: Column
    relation: REL_TYPES
    column2: Column
    config_update: REL_CONFIG | None = None
    config_delete: REL_CONFIG | None = None


@dataclass
class Database(object):
    """Описание схемы БД."""

    project_definition: ProjectDefinition | None = None
    enums: Iterable[Enum] | None = None
    tables: Iterable[Table] | None = None
    relations: Iterable[Relation] | None = None
