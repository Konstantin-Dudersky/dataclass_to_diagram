from typing import Final
from dataclass_to_diagram.models.c4 import C4


TEMPLATE: Final[
    str
] = """@startuml
!include C4_Dynamic.puml
@enduml
"""


def c4_to_puml(c4: C4):
    return TEMPLATE
