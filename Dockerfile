FROM python:alpine
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .
COPY src .

RUN pip install -r requirements.txt

CMD python /app/scheduler.py
