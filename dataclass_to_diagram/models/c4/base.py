from dataclasses import dataclass, field


@dataclass
class BaseElement(object):
    class_name_str: str = field(init=False, default="NotImplemented")
    alias: str = field(init=False)
    label: str
    descr: str | None = None
    techn: str | None = None

    def __post_init__(self) -> None:
        self.alias = str(id(self)).replace("-", "_")