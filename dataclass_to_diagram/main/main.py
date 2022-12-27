"""Точка входа для генерации схем."""

import logging
from pathlib import Path
from types import ModuleType

from rich import print

from ..models.base_model import BaseModel, ModelTypes
from ..exceptions import IncorrectArgError
from ..exporters import ErdToDbml
from .import_modules import import_modules
from .module_info import ModuleInfo
from .prepare_target_folder import prepare_target_folder
from .scan_source_folder_for_modules import scan_source_folder_for_modules

log = logging.getLogger(__name__)


def __search_diagram_in_module(module: ModuleType) -> BaseModel | None:
    """Ищем модели диаграмм в модуле."""
    dias: list[BaseModel] = []
    for item in module.__dict__.values():
        if isinstance(item, BaseModel):
            dias.append(item)
    if not dias:
        return None
    if len(dias) != 1:
        msg: str = (
            "В модуле может находится только одна диаграмма;"
            + "в модуле {0} находится {1} моделей диаграмм."
        ).format(module.__name__, len(dias))
        raise IncorrectArgError(msg)
    log.info(
        "В модуле {0} найдена диаграмма {1}".format(
            module.__name__,
            dias[0].model_type,
        ),
    )
    return dias[0]


def _create_paths_and_check(source: str, target: str) -> tuple[Path, Path]:
    path_source = Path(source)
    path_target = Path(target)
    if not path_source.exists():
        msg = "Папка {0} не найдена!".format(path_source.absolute())
        raise IncorrectArgError(msg)
    log.info("Папка с датаклассами: {0}".format(path_source))
    log.info("Целевая папка: {0}".format(path_target))
    return path_source, path_target


def _export_model_to_str(model: BaseModel) -> tuple[str, str]:
    match model.model_type:
        case ModelTypes.erd:
            ext = ".{0}.dbml".format(model.model_type)
            return (ErdToDbml(model).export(), ext)
        case _:
            msg: str = "Неизвестный тип модели:{0}".format(model.model_type)
            IncorrectArgError(msg)


def _save_model_to_file(model_str: str, filename: Path) -> None:
    with open(filename, "w") as export_file:
        export_file.write(model_str)
    log.info("Модель успешно экспортирована: {0}".format(filename))


def export_models(source: str, target: str) -> None:
    """Экспорт моделей в текстовые файлы.

    Parameters
    ----------
    source: str
        путь к папке с текстовым описанием диаграмм
    target: str
        путь к папке, куда будут сохраняться изображения
    """
    path_source, path_target = _create_paths_and_check(source, target)
    prepare_target_folder(
        path_source=path_source,
        path_target=path_target,
    )
    potential_modules: list[ModuleInfo] = scan_source_folder_for_modules(
        path_source=path_source,
        path_target=path_target,
    )
    imported_modules: list[ModuleInfo] = import_modules(
        potential_modules=potential_modules,
    )
    # экспортируем диаграммы
    for module in imported_modules:
        if module.imported is None:
            continue
        diagram = __search_diagram_in_module(module.imported)
        if diagram is None:
            continue
        model_and_ext = _export_model_to_str(diagram)
        diagram_name = module.imported.__name__.split(".")[-1]
        _save_model_to_file(
            model_str=model_and_ext[0],
            filename=module.path_inside_target
            / "{0}{1}".format(diagram_name, model_and_ext[1]),
        )
