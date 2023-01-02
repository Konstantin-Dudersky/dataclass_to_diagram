from dataclass_to_diagram.models import state_machine

diagram = state_machine.Diagram(
    states=[
        a := state_machine.State(
            "A",
            internal_states=[
                y := state_machine.State("Y"),
                x := state_machine.State("X"),
            ],
        ),
        b := state_machine.State(
            "B",
            internal_states=[
                z := state_machine.State("Z"),
            ],
        ),
    ],
    transitions=[
        state_machine.Transition(x, z),
        state_machine.Transition(z, y),
    ],
)
