# Используем официальный образ Python 3.11
FROM python:3.11

# Рабочая папка внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/

# Устанавливаем их
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем зависимости для psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем весь проект
COPY . /app/

# Запускаем сервер (внимание: 0.0.0.0, а не 127.0.0.1)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]