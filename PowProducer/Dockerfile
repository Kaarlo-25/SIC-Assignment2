FROM python:3.11

WORKDIR /app

RUN pip install kafka-python

COPY power.py .

CMD ["python", "-u", "power.py"]