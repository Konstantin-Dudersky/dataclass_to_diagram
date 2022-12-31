from typing import Final

from dataclass_to_diagram.models.c4 import C4

from .context_to_puml import context_to_puml
from .container_to_puml import container_to_puml
from .rel_to_puml import rel_to_puml
from .sprites_to_puml import sprites_to_puml

TEMPLATE: Final[
    str
] = """@startuml
!include C4_Dynamic.puml{sprites}{contexts}{containers}{relations}{legend}
@enduml
"""


def _export_legend(show_legend: bool) -> str:
    if not show_legend:
        return ""
    return "\nSHOW_LEGEND()"


def c4_to_puml(c4: C4):
    if c4.contexts:
        contexts_list: list[str] = [
            context_to_puml(context) for context in c4.contexts
        ]
        contexts_str = "\n" + "\n".join(contexts_list)
    else:
        contexts_str = ""
    if c4.containers:
        containers_list: list[str] = [
            container_to_puml(container) for container in c4.containers
        ]
        containers_str = "\n" + "\n".join(containers_list)
    else:
        containers_str = ""
    if c4.relations:
        rel_list: list[str] = [rel_to_puml(rel) for rel in c4.relations]
        relations_str = "\n" + "\n".join(rel_list)
    else:
        relations_str = ""
    return TEMPLATE.format(
        sprites=sprites_to_puml(c4.sprites),
        contexts=contexts_str,
        containers=containers_str,
        relations=relations_str,
        legend=_export_legend(c4.show_legend),
    )
