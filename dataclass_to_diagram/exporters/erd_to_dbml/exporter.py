from .database import database_to_dbml
from ..base_exporter import BaseExporter
from ...models.base_model import BaseModel


class Exporter(BaseExporter):
    def __init__(self, model: BaseModel) -> None:
        self.__model = model

    def export(self) -> str:
        """Экспорт модели."""
        return database_to_dbml(self.__model)  # type: ignore
