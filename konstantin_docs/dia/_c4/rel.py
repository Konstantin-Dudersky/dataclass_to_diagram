"""Отношения."""

from konstantin_docs.dia._c4.base import _BaseC4Element


class _RelationKinds():
    """NOTUSED."""

    BIREL = "BiRel"
    REL_UP = "Rel_Up"
    REL_DOWN = "Rel_Down"
    REL_LEFT = "Rel_Left"
    REL_RIGHT = "Rel_Right"


class _BaseRelation:
    """Базовый класс для отношений."""

    def __init__(
        self: "_BaseRelation",
        kind: str,
        link_from: _BaseC4Element,
        link_to: _BaseC4Element,
        label: str,
        techn: str = "",
        descr: str = "",
    ) -> None:
        """Создает Relation."""
        self.__kind = kind
        self.__link_from = link_from
        self.__link_to = link_to
        self.__label = label
        self.__techn = techn
        self.__descr = descr

    def __repr__(self: "_BaseRelation") -> str:
        """Return string representation."""
        template = """
{kind}({link_from}, {link_to}, "{label}", "{techn}", "{descr}")
"""
        return template.format(
            kind=self.__kind,
            link_from=self.__link_from.alias,
            link_to=self.__link_to.alias,
            label=self.__label,
            techn=self.__techn,
            descr=self.__descr,
        )


class Rel(_BaseRelation):
    """Relation."""

    def __init__(
        self: "Rel",
        link_from: _BaseC4Element,
        link_to: _BaseC4Element,
        label: str,
        techn: str = "",
        descr: str = "",
    ) -> None:
        """Создает Relation."""
        super().__init__(
            kind="Rel",
            link_from=link_from,
            link_to=link_to,
            label=label,
            techn=techn,
            descr=descr,
        )


class RelBack(_BaseRelation):
    """RelBack."""

    def __init__(
        self: "RelBack",
        link_from: _BaseC4Element,
        link_to: _BaseC4Element,
        label: str,
        techn: str = "",
        descr: str = "",
    ) -> None:
        """Создает Relation."""
        super().__init__(
            kind="Rel_Back",
            link_from=link_from,
            link_to=link_to,
            label=label,
            techn=techn,
            descr=descr,
        )


class RelNeighbor(_BaseRelation):
    """Rel_Neighbor."""

    def __init__(
        self: "RelNeighbor",
        link_from: _BaseC4Element,
        link_to: _BaseC4Element,
        label: str,
        techn: str = "",
        descr: str = "",
    ) -> None:
        """Создает Relation."""
        super().__init__(
            kind="Rel_Neighbor",
            link_from=link_from,
            link_to=link_to,
            label=label,
            techn=techn,
            descr=descr,
        )
