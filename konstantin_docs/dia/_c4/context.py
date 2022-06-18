"""Уровень 1 - context."""

from enum import Enum

from konstantin_docs.dia._c4.base import _BaseC4Element


class SystemKinds(Enum):
    """Типы персон."""

    PERSON_EXT = "Person_Ext"
    SYSTEMDB = "SystemDb"
    SYSTEMQUEUE = "SystemQueue"
    SYSTEMDB_EXT = "SystemDb_Ext"
    SYSTEMQUEUE_EXT = "SystemQueue_Ext"
    BOUNDARY = "Boundary"
    ENTERPRISE_BOUNDARY = "Enterprise_Boundary"
    SYSTEM_BOUNDARY = "System_Boundary"


TEMPLATE_SYSTEM_BOUNDARY = """
{kind}({alias}, "{label}", "{type}")
"""

TEMPLATE_SYSTEM_XXX_BOUNDARY = """
{kind}({alias}, "{label}")
"""


class _BaseContext(_BaseC4Element):
    """Person."""

    def __init__(
        self: "_BaseContext",
        label: str,
    ) -> None:
        """Создать _BaseContext."""
        super().__init__(
            label=label,
        )

    def __repr__(self: "_BaseContext") -> str:
        """Return string representation."""
        raise NotImplementedError("Метод не переопределен")


class Person(_BaseContext):
    """Person."""

    def __init__(
        self: "Person",
        label: str,
        descr: str = "",
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
        )
        self.__descr = descr

    def __repr__(self: "Person") -> str:
        """Return string representation."""
        template = """
Person({alias}, "{label}", "{descr}")
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
        )


class System(_BaseContext):
    """System."""

    def __init__(
        self: "System",
        label: str,
        descr: str = "",
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
        )
        self.__descr = descr

    def __repr__(self: "System") -> str:
        """Return string representation."""
        template = """
System({alias}, "{label}", "{descr}")
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
        )


class SystemExt(_BaseContext):
    """SystemExt."""

    def __init__(
        self: "SystemExt",
        label: str,
        descr: str = "",
    ) -> None:
        """Создать Person."""
        super().__init__(
            label=label,
        )
        self.__descr = descr

    def __repr__(self: "SystemExt") -> str:
        """Return string representation."""
        template = """
System_Ext({alias}, "{label}", "{descr}")
"""
        return template.format(
            alias=self.alias,
            label=self.label,
            descr=self.__descr,
        )

        # match self.__kind:
        #     case SystemKinds.BOUNDARY:
        #         return TEMPLATE_SYSTEM_BOUNDARY.format(
        #             kind=self.__kind.value,
        #             alias=self.alias,
        #             label=self.label,
        #             type=self.__boundary_type,
        #         )

        #     case SystemKinds.ENTERPRISE_BOUNDARY | SystemKinds.SYSTEM_BOUNDARY:
        #         return TEMPLATE_SYSTEM_XXX_BOUNDARY.format(
        #             kind=self.__kind.value,
        #             alias=self.alias,
        #             label=self.label,
        #         )

        #     case _:
