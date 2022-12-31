"""icons/sprites."""

from dataclass_to_diagram.models import c4

dia = c4.C4(
    contexts=[
        user := c4.context.Person(
            label="Customer",
            descr="People that need products",
            sprite=c4.sprite.tupadr3.FontAwesome5.users,
        ),
    ],
    containers=[
        spa := c4.container.Container(
            label="SPA",
            techn="angular",
            descr="The main interface that the customer interacts with",
            sprite=c4.sprite.tupadr3.FontAwesome5.angular,
        ),
        api := c4.container.Container(
            label="API",
            techn="java",
            descr="Handles all business logic",
            sprite=c4.sprite.tupadr3.FontAwesome5.java,
        ),
        db := c4.container.ContainerDb(
            label="Database",
            techn="Microsoft SQL",
            descr="Holds product, order and invoice information",
            sprite=c4.sprite.tupadr3.Devicons.msql_server,
        ),
    ],
    relations=[
        c4.rel.Rel(begin=user, end=spa, label="Uses", techn="https"),
        c4.rel.Rel(begin=spa, end=api, label="Uses", techn="https"),
        c4.rel.RelRight(begin=api, end=db, label="Reads/Writes"),
    ],
)
