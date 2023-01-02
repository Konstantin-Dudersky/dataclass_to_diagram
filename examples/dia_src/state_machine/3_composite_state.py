from dataclass_to_diagram.models import state_machine

diagram = state_machine.Diagram(
    states=[
        start := state_machine.StateStart(),
        not_shooting := state_machine.State(
            "NotShooting",
            internal_states=[
                start1 := state_machine.StateStart(),
                idle := state_machine.State("Idle"),
            ],
        ),
        configuring := state_machine.State(
            "Configuring",
            internal_states=[
                start2 := state_machine.StateStart(),
                new_value_selection := state_machine.State("NewValueSelection"),
                new_value_preview := state_machine.State(
                    "NewValuePreview",
                    internal_states=[
                        state1 := state_machine.State("State1"),
                        state2 := state_machine.State("State2"),
                    ],
                ),
            ],
        ),
    ],
    transitions=[
        state_machine.Transition(start, not_shooting),
        state_machine.Transition(start1, idle),
        state_machine.Transition(idle, configuring, "EvConfig"),
        state_machine.Transition(configuring, idle, "EvConfig"),
        state_machine.Transition(start2, new_value_selection),
        state_machine.Transition(
            new_value_selection,
            new_value_preview,
            "EvNewValue",
        ),
        state_machine.Transition(
            new_value_preview,
            new_value_selection,
            "EvNewValueRejected",
        ),
        state_machine.Transition(
            new_value_preview,
            new_value_selection,
            "EvNewValueSaved",
        ),
        state_machine.Transition(state1, state2),
    ],
)
