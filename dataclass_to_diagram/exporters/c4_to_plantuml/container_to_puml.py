from dataclass_to_diagram.models.c4.container.containter import (
    BaseContainer,
)

from .base_element_to_puml import base_element_to_puml


def container_to_puml(
    context: BaseContainer,
) -> str:
    args = base_element_to_puml(context)
    args_str_list = [
        "{0}={1}".format(key, value) for key, value in args.items()
    ]
    args_str = ", ".join(args_str_list)
    return "{class_name}({args})".format(
        class_name=context.class_name_str,
        args=args_str,
    )
