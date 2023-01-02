from dataclass_to_diagram.models import state_machine as sm

diagram = sm.Diagram(
    states=[
        idle := sm.State("Idle"),
        req := sm.State("Req(Id)"),
        choice := sm.StateChoice(),
        minor := sm.State("Minor(Id)"),
        major := sm.State("Major(Id)"),
    ],
    transitions=[
        sm.Transition(idle, req),
        sm.Transition(req, choice),
        sm.Transition(choice, minor, "[Id <= 10]"),
        sm.Transition(choice, major, "[Id > 10]"),
    ],
)
