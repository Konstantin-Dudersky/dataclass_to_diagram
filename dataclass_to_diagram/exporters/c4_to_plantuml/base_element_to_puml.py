from dataclass_to_diagram.models.c4.base import BaseElement


def base_element_to_puml(
    base_element: BaseElement,
) -> dict[str, str]:
    args: dict[str, str] = {}
    args["$alias"] = base_element.alias
    args["$label"] = '"{0}"'.format(base_element.label)
    if base_element.descr:
        args["$descr"] = '"{0}"'.format(base_element.descr)
    if base_element.techn:
        args["$techn"] = '"{0}"'.format(base_element.techn)
    if base_element.sprite:
        args["$sprite"] = base_element.sprite.value
    if base_element.link:
        args["$link"] = '"{0}"'.format(base_element.link)
    return args
