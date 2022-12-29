from dataclass_to_diagram.exporters.c4_to_plantuml.c4_to_puml import c4_to_puml
from dataclass_to_diagram.models.c4 import C4


def test_empty():
    c4 = C4()
    puml: str = """@startuml
!include C4_Dynamic.puml
@enduml
"""
    assert c4_to_puml(c4) == puml
