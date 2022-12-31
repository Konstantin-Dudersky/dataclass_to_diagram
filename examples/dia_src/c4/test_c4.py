"""Тест диаграмм C4."""

from dataclass_to_diagram import c4

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
