from types import MappingProxyType
from typing import Type, TypeAlias

from . import converters

TConverters: TypeAlias = MappingProxyType[str, Type[converters.BaseConverter]]
