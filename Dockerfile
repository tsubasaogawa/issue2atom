# syntax = docker/dockerfile:1.3-labs
FROM python:3.8.6

COPY main.py requirements.txt /

RUN <<EOR
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
EOR

ENTRYPOINT ["python", "/main.py"]
