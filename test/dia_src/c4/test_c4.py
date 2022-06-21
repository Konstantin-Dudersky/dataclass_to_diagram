"""Тест диаграмм C4."""

from konstantin_docs.dia.c4 import C4, container, context, rel, sprite, tag

# ex 1 ------------------------------------------------------------------------
person_alias = context.Person(
    label="Label",
    descr="Optional Description",
)
container_alias = container.Container(
    label="Label",
    techn="Technology",
    descr="Optional Description",
)
system_alias = context.System(
    label="Label",
    descr="Optional Description",
)
dia1 = C4(
    filename="dia1",
    title="",
    links_context=[person_alias, system_alias],
    links_container=[container_alias],
    links_rel=[
        rel.Rel(
            links=(person_alias, container_alias),
            label="Label",
            techn="Optional Technology",
        ),
    ],
)

# ex 2 ------------------------------------------------------------------------
admin = context.Person(
    label="Administrator",
)
web_app = container.Container(
    label="Web Application",
    techn="C#, ASP.NET Core 2.1 MVC",
    descr="Allows users to compare multiple Twitter timelines",
)
c1 = context.SystemBoundary(
    label="Sample System",
    links_container=[web_app],
)
twitter = context.System(
    label="Twitter",
)
dia2 = C4(
    filename="dia2",
    title="",
    links_context=[admin, c1, twitter],
    links_rel=[
        rel.Rel(
            links=(admin, web_app),
            label="Uses",
            techn="HTTPS",
        ),
        rel.Rel(
            links=(web_app, twitter),
            label="Gets tweets from",
            techn="HTTPS",
        ),
    ],
)

# ex 3 ------------------------------------------------------------------------
# icons/sprites

user = context.Person(
    label="Customer",
    descr="People that need products",
    sprite=sprite.tupadr3.FontAwesome5(sprite.tupadr3.FontAwesome5Lib.USERS),
)
spa = container.Container(
    label="SPA",
    techn="angular",
    descr="The main interface that the customer interacts with",
    sprite=sprite.tupadr3.FontAwesome5(sprite.tupadr3.FontAwesome5Lib.ANGULAR),
)
api = container.Container(
    label="API",
    techn="java",
    descr="Handles all business logic",
    sprite=sprite.tupadr3.FontAwesome5(sprite.tupadr3.FontAwesome5Lib.JAVA),
)
db = container.ContainerDb(
    label="Database",
    techn="Microsoft SQL",
    descr="Holds product, order and invoice information",
    sprite=sprite.tupadr3.Devicons(sprite.tupadr3.DeviconsLib.MSQL_SERVER),
)
dia3 = C4(
    filename="dia3",
    title="",
    links_context=[user],
    links_container=[spa, api, db],
    links_rel=[
        rel.Rel(
            links=(user, spa),
            label="Uses",
            techn="https",
        ),
        rel.Rel(
            links=(spa, api),
            label="Uses",
            techn="https",
        ),
        rel.RelR(
            links=(api, db),
            label="Reads/Writes",
        ),
    ],
)


# ex 4 ------------------------------------------------------------------------
# links

admin = context.Person(
    label="Administrator",
    sprite=sprite.tupadr3.FontAwesome5(sprite.tupadr3.FontAwesome5Lib.USER),
    link=(
        "https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/"
        "LayoutOptions.md#hide_person_sprite-or-show_person_spritesprite"
    ),
)
web_app = container.Container(
    label="Web Application",
    techn="C#, ASP.NET Core 2.1 MVC",
    descr="Allows users to compare multiple Twitter timelines",
    link=(
        "https://github.com/plantuml-stdlib/C4-PlantUML/blob/master"
        "LayoutOptions.md"
    ),
)
c1 = context.SystemBoundary(
    label="Sample System",
    link="https://github.com/plantuml-stdlib/C4-PlantUML",
    links_container=[web_app],
)
twitter = context.System(
    label="Twitter",
    link="https://github.com/plantuml-stdlib/C4-PlantUML",
)

dia4 = C4(
    filename="dia4",
    title="",
    links_context=[admin, c1, twitter],
    links_rel=[
        rel.Rel(
            links=(admin, web_app),
            label="Uses",
            techn="HTTPS",
            link="https://plantuml.com/link",
        ),
        rel.Rel(
            links=(web_app, twitter),
            label="Gets tweets from",
            techn="HTTPS",
            link="https://plantuml.com/link",
        ),
    ],
)

# ex 5 ------------------------------------------------------------------------
# tags
tag_v_1_0 = tag.ElementTag("v1.0", border_color="#d73027")
tag_v_1_1 = tag.ElementTag("v1.1", font_color="#d73027")
backup = tag.ElementTag("backup", font_color="orange")
backup_rel = tag.RelTag(
    "backup",
    text_color="orange",
    line_color="orange",
    line_style="DashedLine()",
)

user = context.Person("Customer", "People that need products")
admin = context.Person(
    label="Administrator",
    descr="People that administrates the products via the new v1.1 components",
    tags=(tag_v_1_1,),
)
spa = container.Container(
    label="SPA",
    techn="angular",
    descr="The main interface that the customer interacts with via v1.0",
    tags=(tag_v_1_0,),
)
spa_admin = container.Container(
    label="Admin SPA",
    techn="angular",
    descr=(
        "The administrator interface that the customer interacts "
        "with via new v1.1"
    ),
    tags=(tag_v_1_1,),
)
api = container.Container(
    label="API",
    techn="java",
    descr="Handles all business logic (incl. new v1.1 extensions)",
    tags=(tag_v_1_0, tag_v_1_1),
)
db = container.ContainerDb(
    label="Database",
    techn="Microsoft SQL",
    descr="Holds product, order and invoice information",
)
archive = container.Container(
    label="Archive",
    techn="Audit logging",
    descr="Stores 5 years",
    tags=(backup,),
)
dia5 = C4(
    filename="dia5",
    title="",
    links_context=[user, admin],
    links_container=[spa, spa_admin, api, db, archive],
    links_rel=[
        rel.Rel(
            links=(user, spa),
            label="Uses",
            techn="https",
        ),
        rel.Rel(
            links=(spa, api),
            label="Uses",
            techn="https",
        ),
        rel.RelR(
            links=(api, db),
            label="Reads/Writes",
        ),
        rel.Rel(
            links=(admin, spa_admin),
            label="Uses",
            techn="https",
        ),
        rel.Rel(
            links=(spa_admin, api),
            label="Uses",
            techn="https",
        ),
        rel.RelL(
            links=(api, archive),
            label="Writes",
            techn="messages",
            tags=(backup_rel,),
        ),
    ],
)
"""

Rel_L(api, archive, "Writes", "messages", $tags="backup")

@enduml"""

# ex 100 ----------------------------------------------------------------------


customer = context.Person(
    label="Banking Customer",
    descr="A customer of the bank, with personal bank accounts.",
)

banking_system = context.System(
    label="Internet Banking System",
    descr="Allows customers to check their accounts.",
)
mail_system = context.SystemExt(
    label="E-mail system",
    descr="The internal Microsoft Exchange e-mail system.",
)
mainframe = context.SystemExt(
    label="Mainframe Banking System",
    descr="Stores all of the core banking information.",
)


dia100 = C4(
    filename="dia100",
    title="System Context diagram for Internet Banking System",
    links_context=[customer, banking_system, mail_system, mainframe],
    links_rel=[
        rel.Rel(
            links=(customer, banking_system),
            label="Uses",
        ),
        rel.RelBack(
            links=(customer, mail_system),
            label="Sends e-mails to",
        ),
        rel.RelNeighbor(
            links=(banking_system, mail_system),
            label="Sends e-mails",
            techn="SMTP",
        ),
        rel.Rel(
            links=(banking_system, mainframe),
            label="Uses",
        ),
    ],
)
