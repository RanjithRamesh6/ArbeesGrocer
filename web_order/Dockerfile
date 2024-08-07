# Dockerfile for webOrder
FROM python:3.8-slim

WORKDIR /app

COPY web_order.py /app

RUN pip install flask

EXPOSE 5001

CMD ["python", "web_order.py"]
