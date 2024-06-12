# Базовый образ Python
FROM python:3.12-slim

# Установим Poetry
RUN pip install poetry

# Установим рабочую директорию
WORKDIR /app

# Скопируем pyproject.toml и poetry.lock для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Установим зависимости проекта
RUN poetry install --no-root

# Скопируем все файлы проекта в контейнер
COPY . /app

# Укажем команду для запуска приложения
CMD ["poetry", "run", "python", "main.py"]