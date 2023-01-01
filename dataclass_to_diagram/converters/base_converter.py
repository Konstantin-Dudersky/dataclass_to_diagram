"""Базовый конвертер."""

import abc
import logging
from pathlib import Path

log = logging.getLogger(__name__)


class BaseConverter(abc.ABC):
    """Базовый конвертер."""

    @abc.abstractmethod
    async def convert(self, filepath: Path) -> None:
        """Конвертирование."""

    def _log_convert_completed(self, filepath: Path) -> None:
        log.info("Конвертирование выполнено, создан файл: {0}".format(filepath))
