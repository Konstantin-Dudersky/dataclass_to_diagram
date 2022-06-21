"""Уровень 2 - container."""

from .base import BaseC4Element as _BaseC4Element
from .base import BaseSprite as _BaseSprite
from .tag import ElementTag as _ElementTag


class BaseContainer(_BaseC4Element):
    """Person."""

    def __init__(
        self: "BaseContainer",
        label: str,
        sprite: _BaseSprite | None,
        link: str | None,
        tags: tuple[_ElementTag, ...] | None,
    ) -> None:
        """Создать _BaseContainer."""
        super().__init__(
            label=label,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "BaseContainer") -> str:
        """Return string representation."""
        raise NotImplementedError("Метод не переопределен")


class Container(BaseContainer):
    """Container."""

    def __init__(
        self: "Container",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        link: str | None = None,
        tags: tuple[_ElementTag, ...] | None = None,
    ) -> None:
        """Создать Container."""
        super().__init__(
            label=label,
            sprite=sprite,
            link=link,
            tags=tags,
        )
        self.__techn = techn
        self.__descr = descr

    def __repr__(self: "Container") -> str:
        """Return string representation."""
        template = """
Container({alias}, "{label}", "{techn}", "{descr}", $sprite="{sprite}"{tag})
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            techn=self.__techn,
            descr=self.__descr,
            sprite=self.repr_sprite,
            tag=self.repr_tags,
        )


class ContainerDb(BaseContainer):
    """ContainerDb."""

    def __init__(
        self: "ContainerDb",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        link: str | None = None,
        tags: tuple[_ElementTag] | None = None,
    ) -> None:
        """Создать Container."""
        super().__init__(
            label=label,
            sprite=sprite,
            link=link,
            tags=tags,
        )
        self.__techn = techn
        self.__descr = descr

    def __repr__(self: "ContainerDb") -> str:
        """Return string representation."""
        template = """
ContainerDb({alias}, "{label}", "{techn}", "{descr}", $sprite="{sprite}"{tag})
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            techn=self.__techn,
            descr=self.__descr,
            sprite=self.repr_sprite,
            tag=self.repr_tags,
        )
