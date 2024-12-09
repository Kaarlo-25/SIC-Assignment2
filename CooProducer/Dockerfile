FROM python:3.11

WORKDIR /app

RUN pip install kafka-python

COPY cooling.py .

CMD ["python", "-u", "cooling.py"]