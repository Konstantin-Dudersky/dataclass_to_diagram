"""Уровень 2 - container."""

from konstantin_docs.dia._c4.base import _BaseC4Element


class _BaseContainer(_BaseC4Element):
    """Person."""

    def __init__(
        self: "_BaseContainer",
        label: str,
    ) -> None:
        """Создать _BaseContainer."""
        super().__init__(
            label=label,
        )

    def __repr__(self: "_BaseContainer") -> str:
        """Return string representation."""
        raise NotImplementedError("Метод не переопределен")


class Container(_BaseContainer):
    """Container."""

    def __init__(
        self: "Container",
        label: str,
        techn: str = "",
        descr: str = "",
    ) -> None:
        """Создать Container."""
        super().__init__(
            label=label,
        )
        self.__techn = techn
        self.__descr = descr

    def __repr__(self: "Container") -> str:
        """Return string representation."""
        template = """
Container({alias}, "{label}", "{techn}", "{descr}")
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            techn=self.__techn,
            descr=self.__descr,
        )


class ContainerDb(_BaseContainer):
    """ContainerDb."""

    def __init__(
        self: "ContainerDb",
        label: str,
        techn: str = "",
        descr: str = "",
    ) -> None:
        """Создать Container."""
        super().__init__(
            label=label,
        )
        self.__techn = techn
        self.__descr = descr

    def __repr__(self: "ContainerDb") -> str:
        """Return string representation."""
        template = """
ContainerDb({alias}, "{label}", "{techn}", "{descr}")
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            techn=self.__techn,
            descr=self.__descr,
        )
