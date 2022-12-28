"""Точка входа."""

import logging
from types import MappingProxyType

import typer
from rich.logging import RichHandler

from . import converters, main, typings
from .exceptions import BaseError

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler()],
)
logging.getLogger("asyncio").setLevel(logging.WARNING)
log = logging.getLogger(__name__)


CONVERTERS: typings.TConverters = MappingProxyType(
    {
        "**/*.dbml": converters.DbmlConverter,
    },
)


app = typer.Typer()


@app.command()
def export(
    source: str,
    destination: str = typer.Argument("dia_dist"),
) -> None:
    """Экспортировать модели в текстовые файлы."""
    log.info("Скрипт для генерирования диаграмм запущен.")
    try:
        main.export_models(source, destination)
    except BaseError as exc:
        log.critical(exc)


@app.command()
def convert() -> None:
    """Конвертировать текстовые файлы в изображения."""
    main.convert("test/dia_dist", CONVERTERS)


def start():
    """Точка входа."""
    app()
