"""Базовые классы модели."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Iterable


class BaseSprite(StrEnum):
    """Базовый класс для изображений."""

    def include_statements_for_sprite(self) -> set[str]:
        """Возвращает include для спрайтов."""
        raise NotImplementedError


@dataclass
class BaseElement(ABC):
    class_name_str: str = field(init=False, default="NotImplemented")
    alias: str = field(init=False)
    label: str
    descr: str | None = None
    techn: str | None = None
    sprite: BaseSprite | None = None

    def __post_init__(self) -> None:
        self.alias = str(id(self)).replace("-", "_")

    @abstractmethod
    def all_sprites(self) -> set[BaseSprite]:
        """Возвращает include для спрайтов."""
        if self.sprite is None:
            return set()
        return {self.sprite}


@dataclass
class BaseComponent(BaseElement):
    """Уровень 3 - Component."""

    def all_sprites(self) -> set[BaseSprite]:
        return super().all_sprites()


@dataclass
class BaseContainer(BaseElement):
    """Уровень 2 - Container."""

    components: Iterable[BaseComponent] | None = None

    def all_sprites(self) -> set[BaseSprite]:
        """Возвращает include для спрайтов."""
        sprites = super().all_sprites()
        if self.components is None:
            return sprites
        for component in self.components:
            sprites.update(component.all_sprites())
        return sprites


@dataclass
class BaseContext(BaseElement):
    """Уровень 1 - Context."""

    techn: None = field(init=False, default=None)
    containers: Iterable[BaseContainer] | None = None

    def all_sprites(self) -> set[BaseSprite]:
        """Возвращает include для спрайтов."""
        sprites = super().all_sprites()
        if self.containers is None:
            return sprites
        for container in self.containers:
            sprites.update(container.all_sprites())
        return sprites


@dataclass
class BaseRel(object):
    class_name_str: str = field(init=False, default="NotImplemented")
    begin: BaseElement
    end: BaseElement
    label: str
    techn: str | None = None
    descr: str | None = None
