from typing import Final
from dataclass_to_diagram.models.c4.context.context import (
    BaseContext,
)

from .base_element_to_puml import base_element_to_puml
from .container_to_puml import container_to_puml

TEMPLATE: Final[str] = "{class_name}({args}){containers}"


def context_to_puml(
    context: BaseContext,
) -> str:
    args = base_element_to_puml(context)
    args_str_list = [
        "{0}={1}".format(key, value) for key, value in args.items()
    ]
    args_str = ", ".join(args_str_list)
    if context.containers is None:
        containers = ""
    else:
        containers_list: list[str] = []
        for container in context.containers:
            containers_list.append(container_to_puml(container))
        containers_list_joined: str = "\n".join(containers_list)
        containers = "\n{0}".format(containers_list_joined)
        containers = containers.replace("\n", "\n    ")
        containers = "{{{0}\n}}".format(containers)
    return TEMPLATE.format(
        class_name=context.class_name_str,
        args=args_str,
        containers=containers,
    )
