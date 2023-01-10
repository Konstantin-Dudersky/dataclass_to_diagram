from dataclass_to_diagram.models import state_machine as sm

diagram = sm.Diagram(
    states=[
        start1 := sm.StateStart(),
        start2 := sm.StateStart(),
        choice := sm.StateChoice(),
        fork := sm.StateFork(),
        join := sm.StateJoin(),
        state1 := sm.State("State 1"),
        state2 := sm.State("State 2"),
        end1 := sm.StateEnd(),
        end2 := sm.StateEnd(),
    ],
    transitions=[
        sm.Transition(start1, choice, "from start stereo\nto choice"),
        sm.Transition(start2, choice, "from start\nto choice"),
        sm.Transition(choice, fork, "from choice\nto fork"),
        sm.Transition(choice, join, "from choice\nto join"),
        sm.Transition(choice, end1, "from choice\nto end stereo"),
        sm.Transition(fork, state1, "from fork\nto state"),
        sm.Transition(fork, state2, "from fork\nto state"),
        sm.Transition(state1, end2, "from state\nto end"),
        sm.Transition(state2, join, "from state\nto join"),
        sm.Transition(join, end2, "from join\nto end"),
    ],
)
