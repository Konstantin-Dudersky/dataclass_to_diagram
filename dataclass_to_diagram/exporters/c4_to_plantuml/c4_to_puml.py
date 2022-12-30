from typing import Final

from dataclass_to_diagram.models.c4 import C4

from .context_to_puml import context_to_puml
from .rel_to_puml import rel_to_puml

TEMPLATE: Final[
    str
] = """@startuml
!include C4_Dynamic.puml
{contexts}{relations}
@enduml
"""


def c4_to_puml(c4: C4):
    context_list: list[str] = [
        context_to_puml(context) for context in c4.contexts
    ]
    context_str = "\n".join(context_list)
    if c4.relations:
        rel_list: list[str] = [rel_to_puml(rel) for rel in c4.relations]
        relations_str = "\n" + "\n".join(rel_list)
    else:
        relations_str = ""
    return TEMPLATE.format(
        contexts=context_str,
        relations=relations_str,
    )
