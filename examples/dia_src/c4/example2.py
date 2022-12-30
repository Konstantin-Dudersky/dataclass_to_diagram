from dataclass_to_diagram.models import c4

dia = c4.C4(
    contexts=[
        admin := c4.context.Person(
            label="Administrator",
        ),
        c4.context.SystemBoundary(
            label="Sample System",
            containers=[
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
    relations=[
        c4.rel.Rel(
            begin=admin,
            end=web_app,
            label="Uses",
            techn="HTTPS",
        ),
        c4.rel.Rel(
            begin=web_app,
            end=twitter,
            label="Gets tweets from",
            techn="HTTPS",
        ),
    ],
)
