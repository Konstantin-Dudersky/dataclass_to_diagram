"""Точка входа."""

import logging

import typer
from rich.logging import RichHandler

from .main.main import export_models
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
# log.setLevel(logging.DEBUG)

app = typer.Typer()


@app.command()
def export(
    source: str,
    destination: str = typer.Argument("dia_dist"),
) -> None:
    """Генерировать диаграммы."""
    log.info("Скрипт для генерирования диаграмм запущен.")
    try:
        export_models(source, destination)
    except BaseError as exc:
        log.critical(exc)


from .main.convert.convert import convert


@app.command()
def convert1() -> None:
    convert("test/dia_dist")


def main():
    """Точка входа."""
    app()
