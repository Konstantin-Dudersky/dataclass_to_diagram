"""Модель C4.

Описание - https://c4model.com/
Реализация на PlantUML - https://github.com/plantuml-stdlib/C4-PlantUML

"""

import logging

from konstantin_docs.dia._c4 import container, context, rel
from konstantin_docs.dia.base import _BaseDiagram, Image
from konstantin_docs.service.kroki import (
    DiagramTypes,
    OutputFormats,
    get_image,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


# Diagram ---------------------------------------------------------------------

TEMPLATE_DIAGRAM = """@startuml

!include C4_Container.puml

{title}
{context}
{container}
{rels}
@enduml
"""


class C4(_BaseDiagram):
    """Диаграмма C4."""

    def __init__(
        self: "C4",
        filename: str,
        title: str = "Diagram title",
        links_context: list[context._BaseContext] | None = None,
        links_container: list[container._BaseContainer] | None = None,
        links_rel: list[rel._BaseRelation] | None = None,
    ) -> None:
        """Создает объект диаграммы."""
        super().__init__(filename)
        self.__title = title
        self.__links_context = links_context
        self.__links_container = links_container
        self.__link_rels = links_rel

    def get_images(self: "_BaseDiagram") -> tuple[Image]:
        """Возвращает кортеж изображений."""
        images: list[Image] = []
        text = repr(self)
        images.append(self._get_text_file(".puml"))
        # TODO for fmt in (OutputFormats.PNG, OutputFormats.SVG):
        for fmt in (OutputFormats.SVG,):
            images.append(
                Image(
                    filename=self.filename + "." + fmt.value,
                    content=get_image(
                        source=text,
                        diagram_type=DiagramTypes.C4PLANTUML,
                        output_format=fmt,
                    ),
                ),
            )
        return tuple(images)

    def __repr__(self: "C4") -> str:
        """Return string representation."""
        dia = TEMPLATE_DIAGRAM.format(
            title=f"title {self.__title}" if self.__title != "" else "",
            context="".join(
                [repr(context) for context in (self.__links_context or [])],
            ),
            container="".join(
                [
                    repr(container)
                    for container in (self.__links_container or [])
                ],
            ),
            rels="".join([repr(rel) for rel in (self.__link_rels or [])]),
        )
        logger.debug(dia)
        return dia
