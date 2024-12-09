FROM python:3.11

WORKDIR /app

RUN pip install kafka-python

COPY temp3.py .

CMD ["python", "-u", "temp3.py"]