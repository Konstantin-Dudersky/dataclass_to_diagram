from dataclass_to_diagram.models import c4


def test():
    sprites = [
        c4.sprite.tupadr3.Devicons.android,
        c4.sprite.tupadr3.Devicons.angular,
        c4.sprite.tupadr3.Devicons2.babel,
        c4.sprite.tupadr3.Devicons2.backbonejs,
        c4.sprite.tupadr3.FontAwesome5.calculator,
        c4.sprite.tupadr3.FontAwesome5.calendar,
    ]
    dia = c4.C4(
        contexts=[
            c4.context.System(label="", sprite=sprites[0]),
            c4.context.System(
                label="",
                sprite=sprites[1],
                containers=[
                    c4.container.Container(
                        "",
                        sprite=sprites[2],
                        components=[
                            c4.component.Component("", sprite=sprites[3]),
                        ],
                    ),
                    c4.container.Container("", sprite=sprites[4]),
                ],
            ),
        ],
        containers=[c4.container.Container("", sprite=sprites[5])],
    )
    assert dia.sprites is not None
    for sprite in sprites:
        assert sprite in dia.sprites
