# Используйте официальный образ Python
FROM python:3.9-slim

# Установите рабочую директорию
WORKDIR /app

# Копируйте зависимости и установите их
COPY requirements_hao.txt ./
RUN pip install --no-cache-dir -r requirements_hao.txt

# Копируйте исходный код
COPY hao.py ./

# Запустите приложение
CMD ["python", "hao.py"]