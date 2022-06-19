"""Уровень 1 - context."""

from enum import Enum

from konstantin_docs.dia._c4.base import _BaseC4Element
from konstantin_docs.dia._c4.container import _BaseContainer


class SystemKinds(Enum):
    """NOTUSED."""

    SYSTEMDB = "SystemDb"
    SYSTEMQUEUE = "SystemQueue"
    SYSTEMDB_EXT = "SystemDb_Ext"
    SYSTEMQUEUE_EXT = "SystemQueue_Ext"
    ENTERPRISE_BOUNDARY = "Enterprise_Boundary"
    SYSTEM_BOUNDARY = "System_Boundary"


class _BaseContext(_BaseC4Element):
    """Person."""

    def __init__(
        self: "_BaseContext",
        label: str,
        links_container: list[_BaseContainer] | None,
    ) -> None:
        """Создать _BaseContext."""
        super().__init__(
            label=label,
        )
        self.__links_container = links_container

    @property
    def links_container(self: "_BaseContext") -> str:
        """Возвращает список вложенных контейнеров в виде строки."""
        if self.__links_container is None:
            return ""
        links_container_str = "".join(
            [repr(container) for container in self.__links_container],
        )
        return f"""{{
    {links_container_str}
}}"""

    def __repr__(self: "_BaseContext") -> str:
        """Return string representation."""
        raise NotImplementedError("Метод не переопределен")


class Boundary(_BaseContext):
    """System."""

    def __init__(
        self: "Boundary",
        label: str,
        boundary_type: str = "",
        links_container: list[_BaseContainer] | None = None,
    ) -> None:
        """Создать System."""
        super().__init__(
            label=label,
            links_container=links_container,
        )
        self.__boundary_type = boundary_type

    def __repr__(self: "Boundary") -> str:
        """Return string representation."""
        template = """
Boundary({alias}, "{label}", "{type}"){{{links_container}"""
        return template.format(
            alias=self.alias,
            label=self.label,
            type=self.__boundary_type,
            links_container=self.links_container,
        )


class Person(_BaseContext):
    """Person."""

    def __init__(
        self: "Person",
        label: str,
        descr: str = "",
        links_container: list[_BaseContainer] | None = None,
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
            links_container=links_container,
        )
        self.__descr = descr

    def __repr__(self: "Person") -> str:
        """Return string representation."""
        template = """
Person({alias}, "{label}", "{descr}"){links_container}"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
            links_container=self.links_container,
        )


class PersonExt(_BaseContext):
    """PersonExt."""

    def __init__(
        self: "PersonExt",
        label: str,
        descr: str = "",
        links_container: list[_BaseContainer] | None = None,
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
            links_container=links_container,
        )
        self.__descr = descr

    def __repr__(self: "PersonExt") -> str:
        """Return string representation."""
        template = """
Person_Ext({alias}, "{label}", "{descr}"){links_container}"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
            links_container=self.links_container,
        )


class System(_BaseContext):
    """System."""

    def __init__(
        self: "System",
        label: str,
        descr: str = "",
        links_container: list[_BaseContainer] | None = None,
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
            links_container=links_container,
        )
        self.__descr = descr

    def __repr__(self: "System") -> str:
        """Return string representation."""
        template = """
System({alias}, "{label}", "{descr}"){links_container}"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
            links_container=self.links_container,
        )


class SystemBoundary(_BaseContext):
    """SystemBoundary."""

    def __init__(
        self: "SystemBoundary",
        label: str,
        links_container: list[_BaseContainer] | None = None,
    ) -> None:
        """Создать SystemBoundary."""
        super().__init__(
            label=label,
            links_container=links_container,
        )

    def __repr__(self: "SystemBoundary") -> str:
        """Return string representation."""
        template = """
System_Boundary({alias}, "{label}"){links_container}"""
        return template.format(
            alias=self.alias,
            label=self.label,
            links_container=self.links_container,
        )


class SystemExt(_BaseContext):
    """SystemExt."""

    def __init__(
        self: "SystemExt",
        label: str,
        descr: str = "",
        links_container: list[_BaseContainer] | None = None,
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
            links_container=links_container,
        )
        self.__descr = descr

    def __repr__(self: "SystemExt") -> str:
        """Return string representation."""
        template = """
System_Ext({alias}, "{label}", "{descr}"){links_container}"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
            links_container=self.links_container,
        )
