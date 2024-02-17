FROM python:3.12.0

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y postgresql-contrib && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
