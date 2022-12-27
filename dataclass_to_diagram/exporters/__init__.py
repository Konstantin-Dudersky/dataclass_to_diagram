"""Экспорт моделей в текстовый формат."""

from .erd_to_dbml.exporter import Exporter as ErdToDbml

__all__ = [
    "ErdToDbml",
]
