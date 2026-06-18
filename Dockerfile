FROM python:3.11-slim

WORKDIR /app

# závislosti zvlášť kvůli cache vrstvě
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
# default: servíruj API + frontend; build databáze řeší docker-compose (viz command)
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
