"""Level 1 - Context."""

from dataclasses import dataclass, field
from typing import Iterable

from ..base import BaseElement
from ..container.containter import BaseContainer


@dataclass
class BaseContext(BaseElement):
    """Level 1 - Context."""

    techn: None = field(init=False, default=None)
    containers: Iterable[BaseContainer] | None = None


@dataclass
class Person(BaseContext):
    """Level 1 - Context (Person)."""

    class_name_str: str = field(init=False, default="Person")


@dataclass
class PersonExt(BaseContext):
    """Level 1 - Context (Person_Ext)."""

    class_name_str: str = field(init=False, default="Person_Ext")


@dataclass
class System(BaseContext):
    """Level 1 - Context (System)."""

    class_name_str: str = field(init=False, default="System")


@dataclass
class SystemDb(BaseContext):
    """Level 1 - Context (SystemDb)."""

    class_name_str: str = field(init=False, default="SystemDb")


@dataclass
class SystemDbExt(BaseContext):
    """Level 1 - Context (SystemDb_Ext)."""

    class_name_str: str = field(init=False, default="SystemDb_Ext")


@dataclass
class SystemExt(BaseContext):
    """Level 1 - Context (System_Ext)."""

    class_name_str: str = field(init=False, default="System_Ext")


@dataclass
class SystemQueueExt(BaseContext):
    """Level 1 - Context (SystemQueue_Ext)."""

    class_name_str: str = field(init=False, default="SystemQueue_Ext")


@dataclass
class SystemQueue(BaseContext):
    """Level 1 - Context (SystemQueue)."""

    class_name_str: str = field(init=False, default="SystemQueue")


@dataclass
class EnterpriseBoundary(BaseContext):
    """Level 1 - Context (Enterprise_Boundary)."""

    class_name_str: str = field(init=False, default="Enterprise_Boundary")
    descr: None = field(init=False)


@dataclass
class SystemBoundary(BaseContext):
    """Level 1 - Context (System_Boundary)."""

    class_name_str: str = field(init=False, default="System_Boundary")
    descr: None = field(init=False)
