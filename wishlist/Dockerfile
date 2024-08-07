# Dockerfile for wishlist
FROM python:3.8-slim

WORKDIR /app

COPY wishlist.py /app

RUN pip install flask

EXPOSE 5005

CMD ["python", "wishlist.py"]
