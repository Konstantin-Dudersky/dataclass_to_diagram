from dataclasses import dataclass, field
from typing import Iterable

from dataclass_to_diagram.models import BaseModel, ModelTypes

from .base import BaseContainer, BaseContext, BaseRel, BaseSprite


@dataclass
class C4(BaseModel):
    contexts: Iterable[BaseContext] | None = None
    containers: Iterable[BaseContainer] | None = None
    relations: Iterable[BaseRel] | None = None
    show_legend: bool = True
    sprites: Iterable[BaseSprite] | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        """После инициализации полей."""
        super().__init__(ModelTypes.с4)
        self.__find_all_sprites()

    def __find_all_sprites(self) -> None:
        sprites: set[BaseSprite] = set()
        if self.contexts:
            for context in self.contexts:
                sprites.update(context.all_sprites())
        if self.containers:
            for container in self.containers:
                sprites.update(container.all_sprites())
        self.sprites = sprites
