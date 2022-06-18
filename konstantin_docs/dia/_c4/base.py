"""Базовые классы."""


class _BaseC4Element:
    """Базовый элемент диаграмм."""

    def __init__(
        self: "_BaseC4Element",
        label: str,
    ) -> None:
        self.__alias = str(id(self)).replace("-", "_")
        self.__label = label

    @property
    def alias(self: "_BaseC4Element") -> str:
        """Возвращает alias."""
        return self.__alias

    @property
    def label(self: "_BaseC4Element") -> str:
        """Возвращает метку."""
        return self.__label
