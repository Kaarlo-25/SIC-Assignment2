FROM python:3.11

WORKDIR /app

RUN pip install kafka-python

COPY temp1.py .

CMD ["python", "-u", "temp1.py"]