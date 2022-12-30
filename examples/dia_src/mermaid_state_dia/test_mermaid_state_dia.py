"""State for mermaid state diagram."""
from dataclass_to_diagram.dia.mermaid_state.mermaid_state import (
    Diagram,
    Note,
    State,
    Trans,
)


# dia1 -------------------------------------------------------------------------
dia1 = Diagram(
    filename="dia1",
    states=[
        still := State("Still"),
        moving := State("Moving"),
        crash := State("Crash"),
    ],
    trans=[
        Trans(None, still),
        Trans(still, None),
        Trans(still, moving),
        Trans(moving, still),
        Trans(moving, crash),
        Trans(crash, None),
    ],
)

# dia2 -------------------------------------------------------------------------
# composite state

dia2: Diagram = Diagram(
    filename="dia2",
    states=[
        first := State(
            label="First",
            states=[second := State("Second")],
            trans=[
                Trans(None, second),
                Trans(second, None),
            ],
        ),
    ],
    trans=[Trans(None, first)],
)

# dia3 -------------------------------------------------------------------------
# composite state

dia3: Diagram = Diagram(
    filename="dia3",
    states=[
        first := State(
            label="First",
            states=[
                second := State(
                    label="Second",
                    states=[third := State("Third")],
                    trans=[
                        Trans(None, third),
                        Trans(third, None),
                    ],
                ),
            ],
            trans=[
                Trans(None, second),
                Trans(second, None),
            ],
        ),
    ],
    trans=[Trans(None, first)],
)

# dia4 -------------------------------------------------------------------------
# composite state with transitions

dia4: Diagram = Diagram(
    filename="dia4",
    states=[
        first := State(
            "First",
            states=[fir := State("fir")],
            trans=[
                Trans(None, fir),
                Trans(fir, None),
            ],
        ),
        second := State(
            "Second",
            states=[sec := State("sec")],
            trans=[
                Trans(None, sec),
                Trans(sec, None),
            ],
        ),
        third := State(
            "Third",
            states=[thi := State("thi")],
            trans=[
                Trans(None, thi),
                Trans(thi, None),
            ],
        ),
    ],
    trans=[
        Trans(None, first),
        Trans(first, second),
        Trans(first, third),
    ],
)

# dia5 -------------------------------------------------------------------------
# choice

dia5: Diagram = Diagram(
    filename="dia5",
    states=[
        is_positive := State(label="IsPositive"),
        if_state := State(label="IfState", modif=State.ModifEnum.choice),
        false := State(label="False"),
        true := State(label="True"),
    ],
    trans=[
        Trans(None, is_positive),
        Trans(is_positive, if_state),
        Trans(if_state, false, "if n < 0"),
        Trans(if_state, true, "if n > 0"),
    ],
)

# dia6 -------------------------------------------------------------------------
# forks

dia6: Diagram = Diagram(
    filename="dia6",
    states=[
        fork_state := State("ForkState", modif=State.ModifEnum.fork),
        join_state := State("JoinState", modif=State.ModifEnum.join),
        state2 := State("State2"),
        state3 := State("State3"),
        state4 := State("State4"),
    ],
    trans=[
        Trans(None, fork_state),
        Trans(fork_state, state2),
        Trans(fork_state, state3),
        Trans(state2, join_state),
        Trans(state3, join_state),
        Trans(join_state, state4),
        Trans(state4, None),
    ],
)

# dia7 -------------------------------------------------------------------------
# notes

dia7: Diagram = Diagram(
    filename="dia7",
    states=[
        state1 := State(
            "State1",
            note=Note(
                text="Important information! You can write",
                pos=Note.PosEnum.right,
            ),
        ),
        state2 := State(
            "State2",
            note=Note(
                text="This is the note to the left.",
                pos=Note.PosEnum.left,
            ),
        ),
    ],
    trans=[Trans(state1, state2)],
)

# dia8 -------------------------------------------------------------------------
# concurrency

dia8: Diagram = Diagram(
    filename="dia8",
    states=[
        active := State(
            "active",
            states=[
                num_lock_off := State("NumLockOff"),
                num_lock_on := State("NumLockOn"),
            ],
            trans=[
                Trans(None, num_lock_off),
                Trans(num_lock_off, num_lock_on),
                Trans(num_lock_on, num_lock_off),
            ],
        ),
    ],
    trans=[Trans(None, active)],
)
