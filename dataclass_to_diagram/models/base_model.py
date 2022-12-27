"""Базовая модель."""

import abc
import enum


class ModelTypes(enum.StrEnum):
    erd = enum.auto()


class BaseModel(abc.ABC):
    """Базовая модель."""

    def __init__(self, model_type: ModelTypes) -> None:
        self.__model_type = model_type

    @property
    def model_type(self) -> ModelTypes:
        return self.__model_type
