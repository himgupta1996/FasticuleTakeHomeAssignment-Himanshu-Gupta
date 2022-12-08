FROM python:3.9-slim-bullseye

WORKDIR /home
COPY setup.py .
COPY main.py .

RUN apt update && apt upgrade -y

RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir --upgrade -e .

CMD uvicorn main:service --host 0.0.0.0 --port 8001