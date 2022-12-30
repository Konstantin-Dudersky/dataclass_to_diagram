"""Тест диаграмм C4."""

from dataclass_to_diagram import c4

# ex 1 ------------------------------------------------------------------------
dia1: c4.C4 = c4.C4(
    filename="dia1",
    title="",
    links_context=[
        person_alias := c4.context.Person(
            label="Label",
            descr="Optional Description",
        ),
        system_alias := c4.context.System(
            label="Label",
            descr="Optional Description",
        ),
    ],
    links_container=[
        container_alias := c4.container.Container(
            label="Label",
            techn="Technology",
            descr="Optional Description",
        ),
    ],
    links_rel=[
        c4.rel.Rel(
            links=(person_alias, container_alias),
            label="Label",
            techn="Optional Technology",
        ),
    ],
)

# ex 2 ------------------------------------------------------------------------
dia2 = c4.C4(
    filename="dia2",
    title="",
    links_context=[
        admin := c4.context.Person(
            label="Administrator",
        ),
        c4.context.SystemBoundary(
            label="Sample System",
            links_container=[
                web_app := c4.container.Container(
                    label="Web Application",
                    techn="C#, ASP.NET Core 2.1 MVC",
                    descr="Allows users to compare multiple Twitter timelines",
                ),
            ],
        ),
        twitter := c4.context.System(
            label="Twitter",
        ),
    ],
    links_rel=[
        c4.rel.Rel(
            links=(admin, web_app),
            label="Uses",
            techn="HTTPS",
        ),
        c4.rel.Rel(
            links=(web_app, twitter),
            label="Gets tweets from",
            techn="HTTPS",
        ),
    ],
)

# ex 3 ------------------------------------------------------------------------
# icons/sprites
dia3 = c4.C4(
    filename="dia3",
    title="",
    links_context=[
        user := c4.context.Person(
            label="Customer",
            descr="People that need products",
            sprite=c4.sprite.tupadr3.FontAwesome5(
                c4.sprite.tupadr3.FontAwesome5Lib.USERS,
            ),
        ),
    ],
    links_container=[
        spa := c4.container.Container(
            label="SPA",
            techn="angular",
            descr="The main interface that the customer interacts with",
            sprite=c4.sprite.tupadr3.FontAwesome5(
                c4.sprite.tupadr3.FontAwesome5Lib.ANGULAR,
            ),
        ),
        api := c4.container.Container(
            label="API",
            techn="java",
            descr="Handles all business logic",
            sprite=c4.sprite.tupadr3.FontAwesome5(
                c4.sprite.tupadr3.FontAwesome5Lib.JAVA,
            ),
        ),
        db := c4.container.ContainerDb(
            label="Database",
            techn="Microsoft SQL",
            descr="Holds product, order and invoice information",
            sprite=c4.sprite.tupadr3.Devicons(
                c4.sprite.tupadr3.DeviconsLib.MSQL_SERVER,
            ),
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
    ],
)


# ex 4 ------------------------------------------------------------------------
# links

dia4 = c4.C4(
    filename="dia4",
    title="",
    links_context=[
        admin := c4.context.Person(
            label="Administrator",
            sprite=c4.sprite.tupadr3.FontAwesome5(
                c4.sprite.tupadr3.FontAwesome5Lib.USER,
            ),
            link=(
                "https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/"
                "LayoutOptions.md"
                "#hide_person_sprite-or-show_person_spritesprite"
            ),
        ),
        c1 := c4.context.SystemBoundary(
            label="Sample System",
            link="https://github.com/plantuml-stdlib/C4-PlantUML",
            links_container=[
                web_app := c4.container.Container(
                    label="Web Application",
                    techn="C#, ASP.NET Core 2.1 MVC",
                    descr="Allows users to compare multiple Twitter timelines",
                    link=(
                        "https://github.com/plantuml-stdlib/"
                        "C4-PlantUML/blob/master"
                        "LayoutOptions.md"
                    ),
                ),
            ],
        ),
        twitter := c4.context.System(
            label="Twitter",
            link="https://github.com/plantuml-stdlib/C4-PlantUML",
        ),
    ],
    links_rel=[
        c4.rel.Rel(
            links=(admin, web_app),
            label="Uses",
            techn="HTTPS",
            link="https://plantuml.com/link",
        ),
        c4.rel.Rel(
            links=(web_app, twitter),
            label="Gets tweets from",
            techn="HTTPS",
            link="https://plantuml.com/link",
        ),
    ],
)

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
