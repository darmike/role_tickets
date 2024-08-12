# Вибір базового образу
FROM python:3.11.6-alpine3.18
ENV PYTHONUNBUFFERED 1
# Встановлення робочого каталогу в контейнері
WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Відкриття порту, який використовується Django
EXPOSE 8000

# Команда для запуску Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
