# Dockerfile for orderTracking
FROM python:3.8-slim

WORKDIR /app

COPY order_tracking.py /app

RUN pip install flask

EXPOSE 5002

CMD ["python", "order_tracking.py"]
