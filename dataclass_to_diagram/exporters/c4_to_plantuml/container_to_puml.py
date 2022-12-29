from typing import Final
from dataclass_to_diagram.models.c4.container.containter import (
    BaseContainer,
)

from .base_element_to_puml import base_element_to_puml
from .component_to_puml import component_to_puml

TEMPLATE: Final[str] = "{class_name}({args}){components}"


def container_to_puml(
    context: BaseContainer,
) -> str:
    args = base_element_to_puml(context)
    args_str_list = [
        "{0}={1}".format(key, value) for key, value in args.items()
    ]
    args_str = ", ".join(args_str_list)
    if context.components is None:
        components = ""
    else:
        components_list: list[str] = []
        for component in context.components:
            components_list.append(component_to_puml(component))
        components_list_joined: str = "\n".join(components_list)
        components = "\n{0}".format(components_list_joined)
        components = components.replace("\n", "\n    ")
        components = "{{{0}\n}}".format(components)

    return TEMPLATE.format(
        class_name=context.class_name_str,
        args=args_str,
        components=components,
    )