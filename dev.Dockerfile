# Use official Python image
FROM python:3.11-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies if requirements.txt exists
RUN pip install --no-cache-dir -r requirements.txt || true

COPY . .