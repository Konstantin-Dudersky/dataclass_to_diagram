from dataclass_to_diagram.models import state_machine as sm

diagram = sm.Diagram(
    states=[
        start := sm.StateStart(),
        fork := sm.StateFork(),
        state2 := sm.State("State2"),
        state3 := sm.State("State3"),
        join := sm.StateJoin(),
        state4 := sm.State("State4"),
        end := sm.StateEnd(),
    ],
    transitions=[
        sm.Transition(start, fork),
        sm.Transition(fork, state2),
        sm.Transition(fork, state3),
        sm.Transition(state2, join),
        sm.Transition(state3, join),
        sm.Transition(join, state4),
        sm.Transition(state4, end),
    ],
)
