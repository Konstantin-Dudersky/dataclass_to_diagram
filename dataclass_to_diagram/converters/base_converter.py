"""Базовый конвертер."""

import abc
from pathlib import Path


class BaseConverter(abc.ABC):
    """Базовый конвертер."""

    @abc.abstractmethod
    async def convert(self, filepath: Path) -> None:
        """Конвертирование."""

    def _extract_filename(self, filepath: Path) -> str:
        return filepath.name.split(".")[0]

    def _extract_path(self, filepath: Path) -> Path:
        return filepath.parents[0]
