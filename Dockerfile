FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 8081

CMD sh -c "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8081}"
