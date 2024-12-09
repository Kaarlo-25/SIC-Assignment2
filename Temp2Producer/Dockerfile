FROM python:3.11

WORKDIR /app

RUN pip install kafka-python

COPY temp2.py .

CMD ["python", "-u", "temp2.py"]