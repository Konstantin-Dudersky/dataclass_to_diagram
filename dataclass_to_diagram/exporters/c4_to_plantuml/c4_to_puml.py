from typing import Final

from dataclass_to_diagram.models.c4 import C4

from .context_to_puml import context_to_puml

TEMPLATE: Final[
    str
] = """@startuml
!include C4_Dynamic.puml
{contexts}
@enduml
"""


def c4_to_puml(c4: C4):
    context_list: list[str] = [
        context_to_puml(context) for context in c4.contexts
    ]
    context_str = "\n".join(context_list)
    return TEMPLATE.format(
        contexts=context_str,
    )
