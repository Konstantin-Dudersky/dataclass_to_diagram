"""Тест диаграмм C4."""

from dataclass_to_diagram import c4

# ex 5 ------------------------------------------------------------------------
# tags
tag_v_1_0 = c4.tag.ElementTag("v1.0", border_color="#d73027")
tag_v_1_1 = c4.tag.ElementTag("v1.1", font_color="#d73027")
backup = c4.tag.ElementTag("backup", font_color="orange")
backup_rel = c4.tag.RelTag(
    "backup",
    text_color="orange",
    line_color="orange",
    line_style="DashedLine()",
)
dia5 = c4.C4(
    filename="dia5",
    title="",
    links_context=[
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
    links_container=[
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
    links_rel=[
        c4.rel.Rel(
            links=(user, spa),
            label="Uses",
            techn="https",
        ),
        c4.rel.Rel(
            links=(spa, api),
            label="Uses",
            techn="https",
        ),
        c4.rel.RelR(
            links=(api, db),
            label="Reads/Writes",
        ),
        c4.rel.Rel(
            links=(admin, spa_admin),
            label="Uses",
            techn="https",
        ),
        c4.rel.Rel(
            links=(spa_admin, api),
            label="Uses",
            techn="https",
        ),
        c4.rel.RelL(
            links=(api, archive),
            label="Writes",
            techn="messages",
            tags=(backup_rel,),
        ),
    ],
)


# ex 100 ----------------------------------------------------------------------
dia100 = c4.C4(
    filename="dia100",
    title="System Context diagram for Internet Banking System",
    links_context=[
        customer := c4.context.Person(
            label="Banking Customer",
            descr="A customer of the bank, with personal bank accounts.",
        ),
        banking_system := c4.context.System(
            label="Internet Banking System",
            descr="Allows customers to check their accounts.",
        ),
        mail_system := c4.context.SystemExt(
            label="E-mail system",
            descr="The internal Microsoft Exchange e-mail system.",
        ),
        mainframe := c4.context.SystemExt(
            label="Mainframe Banking System",
            descr="Stores all of the core banking information.",
        ),
    ],
    links_rel=[
        c4.rel.Rel(
            links=(customer, banking_system),
            label="Uses",
        ),
        c4.rel.RelBack(
            links=(customer, mail_system),
            label="Sends e-mails to",
        ),
        c4.rel.RelNeighbor(
            links=(banking_system, mail_system),
            label="Sends e-mails",
            techn="SMTP",
        ),
        c4.rel.Rel(
            links=(banking_system, mainframe),
            label="Uses",
        ),
    ],
)