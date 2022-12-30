from dataclasses import dataclass, field


from ..base import BaseRel


@dataclass
class Rel(BaseRel):
    class_name_str: str = field(init=False, default="Rel")


@dataclass
class RelUp(BaseRel):
    class_name_str: str = field(init=False, default="Rel_Up")


@dataclass
class RelDown(BaseRel):
    class_name_str: str = field(init=False, default="Rel_Down")


@dataclass
class RelLeft(BaseRel):
    class_name_str: str = field(init=False, default="Rel_Left")


@dataclass
class RelRight(BaseRel):
    class_name_str: str = field(init=False, default="Rel_Right")


@dataclass
class BiRel(BaseRel):
    class_name_str: str = field(init=False, default="BiRel")


@dataclass
class BiRelUp(BaseRel):
    class_name_str: str = field(init=False, default="BiRel_Up")


@dataclass
class BiRelDown(BaseRel):
    class_name_str: str = field(init=False, default="BiRel_Down")


@dataclass
class BiRelLeft(BaseRel):
    class_name_str: str = field(init=False, default="BiRel_Left")


@dataclass
class BiRelRight(BaseRel):
    class_name_str: str = field(init=False, default="BiRel_Right")
