# python_linters
Маленький репозиторий для доклада о разных линтерах в языке питон: Ruff, Flake8, Pylint

В репозитории находятся экспериментальный код, ЗАКОММЕНТИРОВАННЫЕ примеры конфигураций инструментов и презентация.

# messy_code.py

Небольшой Python-файл с намеренными ошибками и проблемами
разного типа. Используется для демонстрации того, какие проблемы
обнаруживают разные линтеры.

# messy_benchmark.py

Большой файл с большим количеством повторяющихся проблем.
Используется для сравнения времени работы инструментов.

## Установка

Создать виртуальное окружение:
python -m venv .venv

Windows PowerShell:
.venv\Scripts\Activate.ps1

Установить зависимости:
python -m pip install -r requirements.txt

## Запуск:
python -m flake8 messy_code.py
python -m pylint messy_code.py
python -m ruff check messy_code.py
Автоматическое исправление:
python -m ruff check messy_code.py --fix
Показать предполагаемые изменения:
python -m ruff check messy_code.py --diff

Конфигурации находятся в файлах: .flake8, .pylintrc, .ruff.toml

Для сравнения скорости используется messy_benchmark.py.
Пример PowerShell:
Measure-Command {
    python -m flake8 messy_benchmark.py *> $null
}

Measure-Command {
    python -m pylint messy_benchmark.py *> $null
}

Measure-Command {
    python -m ruff check messy_benchmark.py *> $null
}

