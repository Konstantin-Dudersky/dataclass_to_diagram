"""Пользовательские типы данных."""

from types import MappingProxyType
from typing import Type, TypeAlias

from . import converters, exporters, models

TConverters: TypeAlias = MappingProxyType[
    str,
    Type[converters.BaseConverter],
]

TExporters: TypeAlias = MappingProxyType[
    models.ModelTypes,
    Type[exporters.BaseExporter],
]
