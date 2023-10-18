# Используйте официальный образ Python
FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Копируйте зависимости и установите их
COPY requirements_ni.txt ./
RUN pip install --no-cache-dir -r requirements_ni.txt

# Копируйте исходный код
COPY ni.py ./

# Запустите приложение
CMD ["python", "ni.py"]