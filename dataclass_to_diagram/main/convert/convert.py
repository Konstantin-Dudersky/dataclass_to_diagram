"""Конвертировать текстовые файлы в изображения."""

import asyncio
import logging
from pathlib import Path
from typing import Coroutine

from dataclass_to_diagram import exceptions, typings

log = logging.getLogger(__name__)


def _check_folder(folder: Path) -> None:
    if not folder.exists():
        msg: str = "Папка не существует: {0}".format(folder)
        log.critical(msg)
        raise exceptions.IncorrectArgError(msg)


def _find_files_by_pattern(
    path: Path,
    converters: typings.TConverters,
) -> dict[str, list[Path]]:
    """Находим файлы для каждого типа файла.

    Returns
    -------
    Словарь, где ключ - тип файла, значение - список файлов
    """
    files_by_pattern: dict[str, list[Path]] = {}
    for pattern in converters.keys():
        files_by_pattern[pattern] = list(path.glob(pattern))
    return files_by_pattern


def _create_coros_for_patterns(
    files_by_pattern: dict[str, list[Path]],
    converters: typings.TConverters,
) -> list[Coroutine[None, None, None]]:
    coros: list[Coroutine[None, None, None]] = []
    for pattern, files in files_by_pattern.items():
        for file in files:
            coros.append(converters[pattern]().convert(file))
    return coros


async def _run_coros(coros: list[Coroutine[None, None, None]]) -> None:
    async with asyncio.TaskGroup() as tg:
        for coro in coros:
            tg.create_task(coro)


def convert(
    target: str,
    converters: typings.TConverters,
) -> None:
    """Конвертировать текстовые файлы в изображения.

    Parameters
    ----------
    target: str
        Путь к папке с текстовыми файлами
    converters
        Словарь с соответствием типа файла и класса конвертера
    """
    path_target = Path(target)
    _check_folder(path_target)
    log.info("Ищем текстовые файлы в папке: {0}".format(path_target))
    files_by_pattern: dict[str, list[Path]] = _find_files_by_pattern(
        path=path_target,
        converters=converters,
    )
    coros: list[Coroutine[None, None, None]] = _create_coros_for_patterns(
        files_by_pattern=files_by_pattern,
        converters=converters,
    )
    asyncio.run(_run_coros(coros))
