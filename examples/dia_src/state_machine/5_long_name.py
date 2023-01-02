"""Длинное название состояния.

Выходная строка должна быть:
Accumulate Enough Data\nLong state name

На данный момент этого нет.
"""

from dataclass_to_diagram.models import state_machine as sm

diagram = sm.Diagram(
    states=[
        start := sm.StateStart(),
        state1 := sm.State("State1"),
        state2 := sm.State("State2"),
        state3 := sm.State(
            "State3",
            internal_states=[
                internal_start := sm.StateStart(),
                long := sm.State(
                    "Accumulate Enough Data",
                    description="Just a test",
                ),
                process_data := sm.State("ProcessData"),
            ],
        ),
        end := sm.StateEnd(),
    ],
    transitions=[
        sm.Transition(start, state1),
        sm.Transition(state1, state2, "Succeeded"),
        sm.Transition(state2, state3, "Succeeded"),
        sm.Transition(state1, end, "Aborted"),
        sm.Transition(state2, end, "Aborted"),
        sm.Transition(state3, end, "Succeeded / Save Result"),
        sm.Transition(state3, end, "Aborted"),
        sm.Transition(internal_start, long),
        sm.Transition(long, long, "New Data"),
        sm.Transition(long, process_data, "Enough Data"),
    ],
)
