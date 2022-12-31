"""Tags."""

from dataclass_to_diagram.models import c4

tag_v_1_0 = c4.tag.ElementTag("v1.0", border_color="#d73027")
tag_v_1_1 = c4.tag.ElementTag("v1.1", font_color="#d73027")
backup = c4.tag.ElementTag("backup", font_color="orange")
backup_rel = c4.tag.RelationTag(
    "backup",
    text_color="orange",
    line_color="orange",
    line_style="DashedLine()",
)

dia = c4.C4(
    contexts=[
        user := c4.context.Person("Customer", "People that need products"),
        admin := c4.context.Person(
            label="Administrator",
            descr=(
                "People that administrates the products via the "
                "new v1.1 components"
            ),
            tags=(tag_v_1_1,),
        ),
    ],
    containers=[
        spa := c4.container.Container(
            label="SPA",
            techn="angular",
            descr="The main interface that the customer interacts"
            " with via v1.0",
            tags=(tag_v_1_0,),
        ),
        spa_admin := c4.container.Container(
            label="Admin SPA",
            techn="angular",
            descr=(
                "The administrator interface that the customer interacts "
                "with via new v1.1"
            ),
            tags=(tag_v_1_1,),
        ),
        api := c4.container.Container(
            label="API",
            techn="java",
            descr="Handles all business logic (incl. new v1.1 extensions)",
            tags=(tag_v_1_0, tag_v_1_1),
        ),
        db := c4.container.ContainerDb(
            label="Database",
            techn="Microsoft SQL",
            descr="Holds product, order and invoice information",
        ),
        archive := c4.container.Container(
            label="Archive",
            techn="Audit logging",
            descr="Stores 5 years",
            tags=(backup,),
        ),
    ],
    relations=[
        c4.rel.Rel(
            begin=user,
            end=spa,
            label="Uses",
            techn="https",
        ),
        c4.rel.Rel(
            begin=spa,
            end=api,
            label="Uses",
            techn="https",
        ),
        c4.rel.RelRight(
            begin=api,
            end=db,
            label="Reads/Writes",
        ),
        c4.rel.Rel(
            begin=admin,
            end=spa_admin,
            label="Uses",
            techn="https",
        ),
        c4.rel.Rel(
            begin=spa_admin,
            end=api,
            label="Uses",
            techn="https",
        ),
        c4.rel.RelLeft(
            begin=api,
            end=archive,
            label="Writes",
            techn="messages",
            tags=(backup_rel,),
        ),
    ],
)
