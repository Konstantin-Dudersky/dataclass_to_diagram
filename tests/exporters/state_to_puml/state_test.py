from dataclass_to_diagram.exporters.state_to_puml.state_to_puml import (
    state_to_puml,
)

from dataclass_to_diagram.models import state_machine


def test_minimal():
    st = state_machine.State("state1")
    puml: str = """state "state1" as {0}""".format(st.alias)
    assert state_to_puml(st) == puml


def test_description():
    state = state_machine.State("state1", description="description")
    puml: str = """state "state1" as {0}
{0} : description""".format(
        state.alias,
    )
    assert state_to_puml(state) == puml


def test_description_multiline():
    desc1 = "desc line 1\ndesc line 2\ndesc line 3"
    desc2 = """desc line 1
desc line 2
desc line 3"""
    state1 = state_machine.State(
        "state1",
        description=desc1,
    )
    state2 = state_machine.State(
        "state1",
        description=desc2,
    )
    puml: str = """state "state1" as {0}
{0} : desc line 1
{0} : desc line 2
{0} : desc line 3"""
    assert state_to_puml(state1) == puml.format(state1.alias)
    assert state_to_puml(state2) == puml.format(state2.alias)


def test_state_start():
    state = state_machine.StateStart()
    puml: str = "state {0} <<start>>".format(state.alias)
    assert state_to_puml(state) == puml


def test_state_end():
    state = state_machine.StateEnd()
    puml: str = "state {0} <<end>>".format(state.alias)
    assert state_to_puml(state) == puml


def test_internal_states():
    st1 = state_machine.State(
        name="main_state",
        internal_states=[
            st11 := state_machine.State("state11"),
            st12 := state_machine.State("state12"),
        ],
    )
    puml: str = """state "main_state" as {0} {{
    state "state11" as {1}
    state "state12" as {2}
}}""".format(
        st1.alias,
        st11.alias,
        st12.alias,
    )
    print(state_to_puml(st1))
    assert state_to_puml(st1) == puml
