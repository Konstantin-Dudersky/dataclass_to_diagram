"""Тест диаграмм C4."""

from konstantin_docs.dia.c4 import C4, context, rel

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


dia = C4(
    filename="dia1",
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
