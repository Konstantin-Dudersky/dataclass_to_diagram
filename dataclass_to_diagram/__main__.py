"""Точка входа."""

import logging

import typer

from .main.main import export_models
from .exceptions import BaseError

from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler()],
)

app = typer.Typer()


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


@app.command()
def generate(
    source: str,
    destination: str = typer.Argument("dia_dist"),
) -> None:
    """Генерировать диаграммы."""
    log.info("Скрипт для генерирования диаграмм запущен.")
    try:
        export_models(source, destination)
    except BaseError as exc:
        log.critical(exc)


def main():
    """Точка входа."""
    app()
