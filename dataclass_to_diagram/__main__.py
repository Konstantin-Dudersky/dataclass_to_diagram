"""Точка входа."""

import logging
from types import MappingProxyType

import typer

from . import converters, exceptions, exporters, logger, main, models, typings

logger.logger_setup()
log = logging.getLogger(__name__)


EXPORTERS: typings.TExporters = MappingProxyType(
    {
        models.c4.C4: exporters.C4ToPlantuml,
        models.erd.Database: exporters.ErdToDbml,
    },
)

CONVERTERS: typings.TConverters = MappingProxyType(
    {
        "**/*.dbml": converters.DbmlConverter,
    },
)


app = typer.Typer()

ARG_SRC = typer.Argument(
    "dia_src",
    help="Папка с моделями диаграмм",
)
ARG_DIST = typer.Argument(
    "dia_dist",
    help="Папка с экспортированными текстовыми файлами",
)


@app.command()
def export(source: str = ARG_SRC, distribution: str = ARG_DIST) -> None:
    """Экспортировать модели в текстовые файлы."""
    log.info("Запущен экспорт диаграмм.")
    try:
        main.export(source, distribution, EXPORTERS)
    except exceptions.BaseError as exc:
        log.critical(exc)


@app.command()
def convert(distribution: str = ARG_DIST) -> None:
    """Конвертировать текстовые файлы в изображения."""
    log.info("Запущено конвертирование диаграмм.")
    try:
        main.convert("test/dia_dist", CONVERTERS)
    except exceptions.BaseError as exc:
        log.critical(exc)


@app.command()
def process(source: str = ARG_SRC, distribution: str = ARG_DIST) -> None:
    """Экспортировать модели и конвертировать в изображения."""
    export(source, distribution)
    convert(distribution)


def start():
    """Точка входа."""
    app()
