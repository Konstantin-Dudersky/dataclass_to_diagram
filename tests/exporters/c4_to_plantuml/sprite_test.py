from dataclass_to_diagram.exporters.c4_to_plantuml.sprites_to_puml import (
    sprites_to_puml,
)
from dataclass_to_diagram.models.c4.base import BaseSprite
from dataclass_to_diagram.models import c4


def test():
    sprites: list[BaseSprite] = [
        c4.sprite.tupadr3.Devicons.android,
        c4.sprite.tupadr3.Devicons.android,
        c4.sprite.tupadr3.Devicons.angular,
        c4.sprite.tupadr3.Devicons2.aarch64,
        c4.sprite.tupadr3.Devicons2.aftereffects,
        c4.sprite.tupadr3.FontAwesome5._500px,
        c4.sprite.tupadr3.FontAwesome5.accessible_icon,
        c4.sprite.tupadr3.Devicons.android,
    ]
    puml: str = """
!include <tupadr3/common>
!include <tupadr3/devicons/android>
!include <tupadr3/devicons/angular>
!include <tupadr3/devicons2/aarch64>
!include <tupadr3/devicons2/aftereffects>
!include <tupadr3/font-awesome-5/500px>
!include <tupadr3/font-awesome-5/accessible_icon>"""
    assert sprites_to_puml(sprites) == puml
