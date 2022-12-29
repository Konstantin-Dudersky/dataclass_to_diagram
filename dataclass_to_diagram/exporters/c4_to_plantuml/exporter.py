from ..base_exporter import BaseExporter


class Exporter(BaseExporter):
    @property
    def file_extension(self) -> str:
        return ".c4.puml"
