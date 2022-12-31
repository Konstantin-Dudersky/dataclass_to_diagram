from dataclass_to_diagram.models import c4

dia = c4.C4(
    contexts=[
        person := c4.context.Person(
            label="Label",
            descr="Optional Description",
        ),
        system := c4.context.System(
            label="Label",
            descr="Optional Description",
        ),
    ],
    containers=[
        container := c4.container.Container(
            label="Label",
            techn="Technology",
            descr="Optional Description",
        ),
    ],
    relations=[
        c4.rel.Rel(
            begin=person,
            end=container,
            label="Label",
            techn="Optional Technology",
        ),
    ],
)
