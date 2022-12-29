from dataclasses import dataclass, field
from typing import Iterable

from ..base import BaseElement
from ..component.component import BaseComponent


@dataclass
class BaseContainer(BaseElement):
    components: Iterable[BaseComponent] | None = None


@dataclass
class Container(BaseContainer):
    class_name_str: str = field(init=False, default="Container")


@dataclass
class ContainerDb(BaseContainer):
    class_name_str: str = field(init=False, default="ContainerDb")


@dataclass
class ContainerQueue(BaseContainer):
    class_name_str: str = field(init=False, default="ContainerQueue")


@dataclass
class ContainerExt(BaseContainer):
    class_name_str: str = field(init=False, default="Container_Ext")


@dataclass
class ContainerDbExt(BaseContainer):
    class_name_str: str = field(init=False, default="ContainerDb_Ext")


@dataclass
class ContainerQueueExt(BaseContainer):
    class_name_str: str = field(init=False, default="ContainerQueue_Ext")


@dataclass
class ContainerBoundary(BaseContainer):
    class_name_str: str = field(init=False, default="Container_Boundary")
    techn: None = field(init=False, default=None)
