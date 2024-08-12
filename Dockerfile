# Вибір базового образу
FROM python:3.10-slim

# Встановлення робочого каталогу в контейнері
WORKDIR /app

# Копіювання файлів проекту в контейнер
COPY . /app

# Встановлення залежностей
RUN pip install -r requirements.txt

# Відкриття порту, який використовується Django
EXPOSE 8000

# Команда для запуску Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
