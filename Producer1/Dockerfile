FROM python:3.11

WORKDIR /app

RUN pip install kafka-python

COPY humidity.py .

CMD ["python", "-u", "humidity.py"]