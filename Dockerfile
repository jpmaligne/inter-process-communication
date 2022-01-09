FROM python:3.9-slim-bullseye

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN \
    apt-get update --allow-releaseinfo-change && \
    pip install --upgrade pip && \
    pip install --prefix=/usr/local -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
