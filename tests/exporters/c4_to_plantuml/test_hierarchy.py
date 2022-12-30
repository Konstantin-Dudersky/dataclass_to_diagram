from dataclass_to_diagram.models import c4

from dataclass_to_diagram.exporters.c4_to_plantuml.container_to_puml import (
    container_to_puml,
)
from dataclass_to_diagram.exporters.c4_to_plantuml.context_to_puml import (
    context_to_puml,
)


def test_container():
    container = c4.container.Container(
        label="container",
        components=[
            comp1 := c4.component.Component(label="component1"),
            comp2 := c4.component.Component(label="component2"),
        ],
    )
    puml: str = """Container($alias={0}, $label="container") {{
    Component($alias={1}, $label="component1")
    Component($alias={2}, $label="component2")
}}""".format(
        container.alias,
        comp1.alias,
        comp2.alias,
    )
    converted = container_to_puml(container)
    print(converted)
    assert converted == puml


def test_context():
    context = c4.context.System(
        label="context",
        containers=[
            cont1 := c4.container.Container(
                label="container1",
                components=[
                    comp11 := c4.component.Component(label="component11"),
                    comp12 := c4.component.Component(label="component12"),
                ],
            ),
            cont2 := c4.container.Container(label="container2"),
        ],
    )
    puml: str = """System($alias={0}, $label="context") {{
    Container($alias={1}, $label="container1") {{
        Component($alias={3}, $label="component11")
        Component($alias={4}, $label="component12")
    }}
    Container($alias={2}, $label="container2")
}}""".format(
        context.alias,
        cont1.alias,
        cont2.alias,
        comp11.alias,
        comp12.alias,
    )
    exported = context_to_puml(context)
    print(exported)
    assert exported == puml
