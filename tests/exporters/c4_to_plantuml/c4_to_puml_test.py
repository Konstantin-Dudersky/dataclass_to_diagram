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
    tag1 = c4.tag.ElementTag("tag1")
    tag_rel_1 = c4.tag.RelationTag("tag_rel_1")
    dia = c4.C4(
        contexts=[
            user := c4.context.Person(label="user", tags=[tag1]),
            system := c4.context.SystemBoundary(
                label="system",
                containers=[
                    container1 := c4.container.Container(label="container1"),
                    container2 := c4.container.Container(label="container2"),
                ],
            ),
        ],
        containers=[
            high_container := c4.container.Container("high-level container"),
        ],
        relations=[
            c4.rel.Rel(container1, container2, "rel", tags=[tag_rel_1]),
            c4.rel.BiRel(user, container1, "rel"),
        ],
    )
    puml: str = """@startuml
!include C4_Dynamic.puml

AddElementTag($tagStereo="tag1")

AddRelTag($tagStereo="tag_rel_1")

Person($alias={user}, $label="user", $tags="tag1")
System_Boundary($alias={system}, $label="system") {{
    Container($alias={container1}, $label="container1")
    Container($alias={container2}, $label="container2")
}}

Container($alias={high_container}, $label="high-level container")

Rel($from={container1}, $to={container2}, $label="rel", $tags="tag_rel_1")
BiRel($from={user}, $to={container1}, $label="rel")

SHOW_LEGEND()
@enduml
""".format(
        user=user.alias,
        system=system.alias,
        container1=container1.alias,
        container2=container2.alias,
        high_container=high_container.alias,
    )
    exported = c4_to_puml(dia)
    print(exported)
    assert exported == puml
