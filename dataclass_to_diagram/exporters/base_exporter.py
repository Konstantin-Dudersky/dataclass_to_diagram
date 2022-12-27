"""Базовый класс для экспорта модели в текстовое представление."""

import abc


class BaseExporter(abc.ABC):
    """Базовый класс для экспорта модели в текстовое представление."""

    @abc.abstractmethod
    def export(self) -> str:
        """Экспорт модели."""
