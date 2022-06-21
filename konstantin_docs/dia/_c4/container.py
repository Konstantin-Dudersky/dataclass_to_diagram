"""Уровень 2 - container."""

from .base import BaseC4Element as _BaseC4Element
from .base import BaseSprite as _BaseSprite
from .tag import ElementTag as _ElementTag


class BaseContainer(_BaseC4Element):
    """BaseContainer."""

    def __init__(
        self: "BaseContainer",
        label: str,
        techn: str | None,
        descr: str | None,
        sprite: _BaseSprite | None,
        tags: tuple[_ElementTag, ...] | None,
        link: str | None,
    ) -> None:
        """Создать BaseContainer."""
        super().__init__(
            label=label,
            sprite=sprite,
            link=link,
            tags=tags,
        )
        self.__techn = techn
        self.__descr = descr

    @property
    def _repr_inside_pths(self: "BaseContainer") -> str:
        """Возвращает содержимое внутри скобок + вложенные компоненты."""
        # TODO - вложенные компоненты
        return "({alias}{label}{techn}{descr}{sprite}{tags}{link})\n".format(
            alias=self.format_alias,
            label=self._format_label,
            techn=self._repr_if_not_none("techn", self.__techn),
            descr=self._repr_if_not_none("descr", self.__descr),
            sprite=self._format_sprite,
            tags=self._format_tags,
            link=self._format_link,
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
        tags: tuple[_ElementTag, ...] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать Container."""
        super().__init__(
            label=label,
            techn=techn,
            descr=descr,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "Container") -> str:
        """Return string representation."""
        return f"Container{self._repr_inside_pths}"


class ContainerDb(BaseContainer):
    """ContainerDb."""

    def __init__(
        self: "ContainerDb",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        tags: tuple[_ElementTag] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать ContainerDb."""
        super().__init__(
            label=label,
            descr=descr,
            techn=techn,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "ContainerDb") -> str:
        """Return string representation."""
        return f"ContainerDb{self._repr_inside_pths}"


class ContainerQueue(BaseContainer):
    """ContainerQueue."""

    def __init__(
        self: "ContainerQueue",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        tags: tuple[_ElementTag] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать ContainerQueue."""
        super().__init__(
            label=label,
            descr=descr,
            techn=techn,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "ContainerQueue") -> str:
        """Return string representation."""
        return f"ContainerQueue{self._repr_inside_pths}"


class ContainerExt(BaseContainer):
    """ContainerExt."""

    def __init__(
        self: "ContainerExt",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        tags: tuple[_ElementTag] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать ContainerExt."""
        super().__init__(
            label=label,
            descr=descr,
            techn=techn,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "ContainerExt") -> str:
        """Return string representation."""
        return f"Container_Ext{self._repr_inside_pths}"


class ContainerDbExt(BaseContainer):
    """ContainerDbExt."""

    def __init__(
        self: "ContainerDbExt",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        tags: tuple[_ElementTag] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать ContainerDbExt."""
        super().__init__(
            label=label,
            descr=descr,
            techn=techn,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "ContainerDbExt") -> str:
        """Return string representation."""
        return f"ContainerDb_Ext{self._repr_inside_pths}"


class ContainerQueueExt(BaseContainer):
    """ContainerQueueExt."""

    def __init__(
        self: "ContainerQueueExt",
        label: str,
        techn: str = "",
        descr: str = "",
        sprite: _BaseSprite | None = None,
        tags: tuple[_ElementTag] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать ContainerQueueExt."""
        super().__init__(
            label=label,
            descr=descr,
            techn=techn,
            sprite=sprite,
            link=link,
            tags=tags,
        )

    def __repr__(self: "ContainerQueueExt") -> str:
        """Return string representation."""
        return f"ContainerQueue_Ext{self._repr_inside_pths}"


class ContainerBoundary(BaseContainer):
    """ContainerBoundary."""

    def __init__(
        self: "ContainerBoundary",
        label: str,
        tags: tuple[_ElementTag] | None = None,
        link: str | None = None,
    ) -> None:
        """Создать ContainerBoundary."""
        super().__init__(
            label=label,
            descr=None,
            techn=None,
            sprite=None,
            link=link,
            tags=tags,
        )

    def __repr__(self: "ContainerBoundary") -> str:
        """Return string representation."""
        return f"Container_Boundary{self._repr_inside_pths}"
