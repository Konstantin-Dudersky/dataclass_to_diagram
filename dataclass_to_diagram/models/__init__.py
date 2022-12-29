"""Модели диаграмм разных типов."""

from . import erd
from .base_model import BaseModel, ModelTypes

__all__ = [
    "erd",
    "BaseModel",
    "ModelTypes",
]
