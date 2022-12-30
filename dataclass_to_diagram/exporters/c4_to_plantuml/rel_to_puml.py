from typing import Final

from dataclass_to_diagram.models.c4.base import BaseRel

TEMPLATE: Final[str] = "{class_name}({args})"


def rel_to_puml(rel: BaseRel) -> str:
    args: dict[str, str] = {}
    args["$from"] = rel.begin.alias
    args["$to"] = rel.end.alias
    args["$label"] = '"{0}"'.format(rel.label)
    if rel.techn is not None:
        args["$techn"] = '"{0}"'.format(rel.techn)
    if rel.descr is not None:
        args["$descr"] = '"{0}"'.format(rel.descr)
    args_str_list = [
        "{0}={1}".format(key, value) for key, value in args.items()
    ]
    args_str = ", ".join(args_str_list)
    return TEMPLATE.format(
        class_name=rel.class_name_str,
        args=args_str,
    )
