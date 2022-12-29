from dataclasses import dataclass, field

from ..base import BaseElement


@dataclass
class BaseContext(BaseElement):
    techn: None = field(init=False, default=None)


@dataclass
class Person(BaseContext):
    class_name_str: str = field(init=False, default="Person")


@dataclass
class PersonExt(BaseContext):
    class_name_str: str = field(init=False, default="Person_Ext")


@dataclass
class System(BaseContext):
    class_name_str: str = field(init=False, default="System")


@dataclass
class SystemDb(BaseContext):
    class_name_str: str = field(init=False, default="SystemDb")


@dataclass
class SystemDbExt(BaseContext):
    class_name_str: str = field(init=False, default="SystemDb_Ext")


@dataclass
class SystemExt(BaseContext):
    class_name_str: str = field(init=False, default="System_Ext")


@dataclass
class SystemQueueExt(BaseContext):
    class_name_str: str = field(init=False, default="SystemQueue_Ext")


@dataclass
class SystemQueue(BaseContext):
    class_name_str: str = field(init=False, default="SystemQueue")


@dataclass
class EnterpriseBoundary(BaseContext):
    class_name_str: str = field(init=False, default="Enterprise_Boundary")
    descr: None = field(init=False)


@dataclass
class SystemBoundary(BaseContext):
    class_name_str: str = field(init=False, default="System_Boundary")
    descr: None = field(init=False)
