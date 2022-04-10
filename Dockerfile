FROM python:3.8.6

COPY main.py requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/main.py"]
