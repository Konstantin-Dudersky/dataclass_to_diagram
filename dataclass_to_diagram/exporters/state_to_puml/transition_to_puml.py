from dataclass_to_diagram.models import state_machine

TEMPLATE: str = """{begin} --> {end}{description}"""


def _export_description(description: str | None) -> str:
    if not description:
        return ""
    return " : {0}".format(description)


def transition_to_puml(transition: state_machine.Transition) -> str:
    return TEMPLATE.format(
        begin=transition.begin.alias,
        end=transition.end.alias,
        description=_export_description(transition.description),
    )
