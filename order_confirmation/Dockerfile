# Dockerfile for orderConfirmation
FROM python:3.8-slim

WORKDIR /app

COPY order_confirmation.py /app

RUN pip install flask

EXPOSE 5003

CMD ["python", "order_confirmation.py"]
