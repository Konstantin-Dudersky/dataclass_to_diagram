from dataclasses import dataclass, field

from ..base import BaseElement


@dataclass
class BaseComponent(BaseElement):
    pass


@dataclass
class Component(BaseComponent):
    class_name_str: str = field(init=False, default="Component")


@dataclass
class ComponentDb(BaseComponent):
    class_name_str: str = field(init=False, default="ComponentDb")


@dataclass
class ComponentQueue(BaseComponent):
    class_name_str: str = field(init=False, default="ComponentQueue")


@dataclass
class ComponentExt(BaseComponent):
    class_name_str: str = field(init=False, default="Component_Ext")


@dataclass
class ComponentDbExt(BaseComponent):
    class_name_str: str = field(init=False, default="ComponentDb_Ext")


@dataclass
class ComponentQueueExt(BaseComponent):
    class_name_str: str = field(init=False, default="ComponentQueue_Ext")
