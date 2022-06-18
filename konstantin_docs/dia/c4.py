"""Модель C4.

Описание - https://c4model.com/
Реализация на PlantUML - https://github.com/plantuml-stdlib/C4-PlantUML


"""

from konstantin_docs.dia._c4 import context, rel
from konstantin_docs.dia.base import BaseDiagram, Image
from konstantin_docs.service.kroki import (
    DiagramTypes,
    OutputFormats,
    get_image,
)


# Diagram ---------------------------------------------------------------------

TEMPLATE_DIAGRAM = """
@startuml

!include C4_Container.puml

title {title}
{context}
{rels}
@enduml
"""


class C4(BaseDiagram):
    """Диаграмма C4."""

    def __init__(
        self: "C4",
        filename: str,
        title: str = "Diagram title",
        links_context: list[context._BaseContext] | None = None,
        links_rel: list[rel._BaseRelation] | None = None,
    ) -> None:
        """Создает объект диаграммы."""
        super().__init__(filename)
        self.__title = title
        self.__links_context = links_context
        self.__link_rels = links_rel

    def get_images(self: "BaseDiagram") -> tuple[Image]:
        """Возвращает кортеж изображений."""
        images: list[Image] = []
        for fmt in (OutputFormats.PNG, OutputFormats.SVG):
            images.append(
                Image(
                    filename=self.filename + "." + fmt.value,
                    content=get_image(
                        source=repr(self),
                        diagram_type=DiagramTypes.C4PLANTUML,
                        output_format=fmt,
                    ),
                ),
            )
        return tuple(images)

    def __repr__(self: "C4") -> str:
        """Return string representation."""
        return TEMPLATE_DIAGRAM.format(
            title=self.__title,
            context="".join(
                [repr(context) for context in (self.__links_context or [])],
            ),
            rels="".join([repr(rel) for rel in (self.__link_rels or [])]),
        )
