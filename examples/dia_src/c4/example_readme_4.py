"""Links."""

from dataclass_to_diagram.models import c4

dia = c4.C4(
    contexts=[
        admin := c4.context.Person(
            label="Administrator",
            sprite=c4.sprite.tupadr3.FontAwesome5.user,
            link=(
                "https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/"
                "LayoutOptions.md"
                "#hide_person_sprite-or-show_person_spritesprite"
            ),
        ),
        c1 := c4.context.SystemBoundary(
            label="Sample System",
            link="https://github.com/plantuml-stdlib/C4-PlantUML",
            containers=[
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
    relations=[
        c4.rel.Rel(
            begin=admin,
            end=web_app,
            label="Uses",
            techn="HTTPS",
            link="https://plantuml.com/link",
        ),
        c4.rel.Rel(
            begin=web_app,
            end=twitter,
            label="Gets tweets from",
            techn="HTTPS",
            link="https://plantuml.com/link",
        ),
    ],
    show_legend=False,
)
