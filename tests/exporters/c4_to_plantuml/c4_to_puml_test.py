from dataclass_to_diagram.exporters.c4_to_plantuml.c4_to_puml import c4_to_puml
from dataclass_to_diagram.models import c4


def test_empty():
    dia = c4.C4(show_legend=False)
    puml: str = """@startuml
!include C4_Dynamic.puml
@enduml
"""
    assert c4_to_puml(dia) == puml


def test_show_legend():
    dia = c4.C4(show_legend=True)
    puml: str = """@startuml
!include C4_Dynamic.puml
SHOW_LEGEND()
@enduml
"""
    assert c4_to_puml(dia) == puml


def test_full():
    dia = c4.C4(
        contexts=[
            user := c4.context.Person(label="user"),
            system := c4.context.SystemBoundary(
                label="system",
                containers=[
                    container1 := c4.container.Container(label="container1"),
                    container2 := c4.container.Container(label="container2"),
                ],
            ),
        ],
        relations=[
            c4.rel.Rel(container1, container2, "rel"),
            c4.rel.BiRel(user, container1, "rel"),
        ],
    )
    puml: str = """@startuml
!include C4_Dynamic.puml
Person($alias={user}, $label="user")
System_Boundary($alias={system}, $label="system") {{
    Container($alias={container1}, $label="container1")
    Container($alias={container2}, $label="container2")
}}
Rel($from={container1}, $to={container2}, $label="rel")
BiRel($from={user}, $to={container1}, $label="rel")
SHOW_LEGEND()
@enduml
""".format(
        user=user.alias,
        system=system.alias,
        container1=container1.alias,
        container2=container2.alias,
    )
    exported = c4_to_puml(dia)
    print(exported)
    assert exported == puml
