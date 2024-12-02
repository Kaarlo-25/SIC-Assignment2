import os
import time
import random
from kafka import KafkaProducer

# Load environment variables
mean_humidity = float(os.getenv('MEAN_HUMIDITY'))  # Mean value from environment
std_humidity = float(os.getenv('STD_HUMIDITY'))    # Std deviation from environment
kafka_broker = os.getenv('KAFKA_BROKER')          # Kafka broker
kafka_topic = os.getenv('KAFKA_TOPIC')            # Kafka topic name

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_broker,
    value_serializer=lambda v: v.encode('utf-8')
)

def simulate_humidity(sensor_name):
    """Simulate a humidity reading for a given sensor."""
    humidity = max(0, min(100, random.gauss(mean_humidity, std_humidity)))
    timestamp = int(time.time() * 1e9)  # Nanoseconds since epoch
    return f"{sensor_name} humidity={humidity:.2f} {timestamp}"

try:
    print("Starting humidity simulation...")
    while True:
        for sensor in ["sensor1", "sensor2", "sensor3"]:
            data = simulate_humidity(sensor)
            producer.send(kafka_topic, data)
            print(f"Sent to Kafka: {data}")
        time.sleep(30)  # Wait for 30 seconds
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")
finally:
    producer.close()
    print("Kafka producer closed.")
