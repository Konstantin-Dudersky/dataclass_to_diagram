from dataclass_to_diagram.models import state_machine

diagram = state_machine.Diagram(
    states=[
        start := state_machine.StateStart(),
        state1 := state_machine.State(
            "State1",
            description="this is a string\nthis is another string",
        ),
        state2 := state_machine.State("State2"),
        end := state_machine.StateEnd(),
    ],
    transitions=[
        state_machine.Transition(start, state1),
        state_machine.Transition(state1, state2),
        state_machine.Transition(state1, end),
        state_machine.Transition(state2, end),
    ],
)
