from dataclass_to_diagram.exporters.state_to_puml.transition_to_puml import (
    transition_to_puml,
)
from dataclass_to_diagram.models import state_machine


def test_minimal():
    st1 = state_machine.State("begin")
    st2 = state_machine.State("end")
    trans = state_machine.Transition(st1, st2)
    puml = "{0} --> {1}".format(st1.alias, st2.alias)
    assert transition_to_puml(trans) == puml


def test_with_description():
    st1 = state_machine.State("begin")
    st2 = state_machine.State("end")
    trans = state_machine.Transition(st1, st2, description="description")
    puml = "{0} --> {1} : description".format(st1.alias, st2.alias)
    assert transition_to_puml(trans) == puml
