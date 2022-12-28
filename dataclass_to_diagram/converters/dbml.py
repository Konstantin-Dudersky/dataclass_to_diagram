"""Конвертирование диаграмм баз данных с помощью dbml-renderer."""

import logging
from pathlib import Path
from typing import Any, Final

from dataclass_to_diagram.shared.run_process_async import run_process_async

from .base_converter import BaseConverter

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


COMMAND: Final[str] = "dbml-renderer -i {input} -o {output}"


class DbmlConverter(BaseConverter):
    """Конвертирование dbml."""

    def __init__(self, **kwargs: Any) -> None:
        """Конвертирование dbml."""

    async def convert(self, filepath: Path) -> None:
        """Конвертирование."""
        await run_process_async(
            COMMAND.format(
                input=filepath,
                output="{path}/{filename}.svg".format(
                    path=self._extract_path(filepath),
                    filename=self._extract_filename(filepath),
                ),
            ),
        )