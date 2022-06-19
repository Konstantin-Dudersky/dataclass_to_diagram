"""Тест диаграмм C4."""

from konstantin_docs.dia.c4 import C4, container, context, rel


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
            link_from=person_alias,
            link_to=container_alias,
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
            link_from=admin,
            link_to=web_app,
            label="Uses",
            techn="HTTPS",
        ),
        rel.Rel(
            link_from=web_app,
            link_to=twitter,
            label="Gets tweets from",
            techn="HTTPS",
        ),
    ],
)

# ex 3 ------------------------------------------------------------------------

user = context.Person(
    label="Customer",
    descr="People that need products",
)
spa = container.Container(
    label="SPA",
    techn="angular",
    descr="The main interface that the customer interacts with",
)
api = container.Container(
    label="API",
    techn="java",
    descr="Handles all business logic",
)
db = container.ContainerDb(
    label="Database",
    techn="Microsoft SQL",
    descr="Holds product, order and invoice information",
)
dia3 = C4(
    filename="dia3",
    title="",
    links_context=[user],
    links_container=[spa, api, db],
    links_rel=[
        rel.Rel(
            link_from=user,
            link_to=spa,
            label="Uses",
            techn="https",
        ),
        rel.Rel(
            link_from=spa,
            link_to=api,
            label="Uses",
            techn="https",
        ),
        rel.RelR(
            link_from=api,
            link_to=db,
            label="Reads/Writes",
        ),
    ],
)

# !define DEVICONS https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/devicons
# !define FONTAWESOME https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/font-awesome-5
# !include DEVICONS/angular.puml
# !include DEVICONS/java.puml
# !include DEVICONS/msql_server.puml
# !include FONTAWESOME/users.puml

# LAYOUT_WITH_LEGEND()

# Person(user, "Customer", "People that need products", $sprite="users")
# Container(spa, "SPA", "angular", "The main interface that the customer interacts with", $sprite="angular")
# Container(api, "API", "java", "Handles all business logic", $sprite="java")
# ContainerDb(db, "Database", "Microsoft SQL", "Holds product, order and invoice information", $sprite="msql_server")

# Rel(user, spa, "Uses", "https")
# Rel(spa, api, "Uses", "https")
# Rel_R(api, db, "Reads/Writes")
# @enduml

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
            link_from=customer,
            link_to=banking_system,
            label="Uses",
        ),
        rel.RelBack(
            link_from=customer,
            link_to=mail_system,
            label="Sends e-mails to",
        ),
        rel.RelNeighbor(
            link_from=banking_system,
            link_to=mail_system,
            label="Sends e-mails",
            techn="SMTP",
        ),
        rel.Rel(
            link_from=banking_system,
            link_to=mainframe,
            label="Uses",
        ),
    ],
)
