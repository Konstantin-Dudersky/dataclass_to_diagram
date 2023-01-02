from dataclass_to_diagram.models import state_machine
from dataclass_to_diagram.exporters.state_to_puml.diagram_to_puml import (
    diagram_to_puml,
)


def test_empty():
    dia = state_machine.Diagram()
    puml = """@startuml

@enduml
"""
    assert diagram_to_puml(dia) == puml


def test_hide_empty_desc():
    dia = state_machine.Diagram(hide_empty_description=True)
    puml = """@startuml

hide empty description

@enduml
"""
    assert diagram_to_puml(dia) == puml


def test_full():
    dia = state_machine.Diagram(
        states=[
            state1 := state_machine.State("state1"),
            state2 := state_machine.State(
                "state2",
                internal_states=[
                    state21 := state_machine.State("state21"),
                    state22 := state_machine.State("state22"),
                ],
            ),
        ],
    )
    puml = """@startuml

state "state1" as {0}
state "state2" as {1} {{
    state "state21" as {2}
    state "state22" as {3}
}}

@enduml
""".format(
        state1.alias,
        state2.alias,
        state21.alias,
        state22.alias,
    )
    exported = diagram_to_puml(dia)
    print(exported)
    assert exported == puml
