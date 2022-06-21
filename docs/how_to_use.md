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

Дополнительно для vs code можно создать задачу в файле .vscode/tasks.json:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "docs",
            "type": "shell",
            "command": "poetry run poe docs"
        }
    ]
}
```

## Создание диаграмм

Примеры - https://github.com/Konstantin-Dudersky/konstantin_docs/tree/main/test

В папке dia_src исходные файлы изображений, в папке dia_dist - сгенерированные изображения.

## Запуск

```sh
poetry run poe docs
```

