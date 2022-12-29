"""Базовая модель."""

import abc
import enum


class ModelTypes(enum.StrEnum):
    """Типы моделей."""

    erd = enum.auto()
    с4 = enum.auto()  # noqa: WPS119


class BaseModel(abc.ABC):
    """Базовая модель."""

    def __init__(self, model_type: ModelTypes) -> None:
        """Базовая модель."""
        self.__model_type = model_type

    @property
    def model_type(self) -> ModelTypes:
        """Тип модели."""
        return self.__model_type
