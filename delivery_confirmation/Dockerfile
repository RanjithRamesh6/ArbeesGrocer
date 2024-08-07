# Dockerfile for deliveryConfirmation
FROM python:3.8-slim

WORKDIR /app

COPY delivery_confirmation.py /app

RUN pip install flask

EXPOSE 5004

CMD ["python", "delivery_confirmation.py"]
