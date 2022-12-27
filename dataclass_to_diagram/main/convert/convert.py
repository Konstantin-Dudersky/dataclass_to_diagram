"""Преобразование экспортированных моделей в изображения."""

import asyncio
import logging
from pathlib import Path

from dataclass_to_diagram.converters.dbml import DbmlConverter
from dataclass_to_diagram.exceptions import IncorrectArgError

log = logging.getLogger(__name__)


def convert(target: str) -> None:
    """Преобразование экспортированных моделей в изображения."""
    path = Path(target)
    if not path.exists():
        msg: str = "Папка не существует: {0}".format(path)
        log.critical(msg)
        raise IncorrectArgError(msg)
    log.info("Ищем текстовые файлы в папке: {0}".format(path))
    # найти рекурсивно все файлы
    # для каждого файла вызвать функцию для генерации
    asyncio.run(DbmlConverter().convert(path / "erd/database.erd.dbml"))
