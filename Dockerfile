FROM python:3.11-slim

# 1. Установка системных зависимостей ДО pip-пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 2. Рабочая директория
WORKDIR /app

# 3. Копируем и устанавливаем Python-зависимости
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/development.txt

# 4. Копируем код
COPY . /app/

# 5. Запуск
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]