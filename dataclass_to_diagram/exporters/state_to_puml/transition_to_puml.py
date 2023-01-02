from dataclass_to_diagram.models import state_machine

TEMPLATE: str = """{begin} --> {end}"""


def transition_to_puml(transition: state_machine.Transition) -> str:
    return TEMPLATE.format(
        begin=transition.begin.alias,
        end=transition.end.alias,
    )
