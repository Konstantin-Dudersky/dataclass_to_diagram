# Как использовать

## Настройка

Прописать в файле pyproject.toml:

```toml
[tool.poetry.dependencies]
konstantin_docs = "*"
poethepoet = "*"

[tool.poe.tasks]
docs = {script = "konstantin_docs.main:generate_images('dia_src', 'dia_dist')"}
```

## Создание диаграмм

Примеры - https://github.com/Konstantin-Dudersky/konstantin_docs/tree/main/test

В папке dia_src исходные файлы изображений, в папке dia_dist - сгенерированные изображения.

## Запуск

```sh
poetry run poe docs
```

