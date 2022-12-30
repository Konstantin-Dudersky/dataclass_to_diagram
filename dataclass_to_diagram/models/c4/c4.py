from dataclasses import dataclass
from typing import Iterable

from dataclass_to_diagram.models import BaseModel, ModelTypes

from .context.context import BaseContext
from .base import BaseRel


@dataclass
class C4(BaseModel):
    contexts: Iterable[BaseContext]
    relations: Iterable[BaseRel] | None = None

    def __post_init__(self) -> None:
        """После инициализации полей."""
        super().__init__(ModelTypes.с4)
