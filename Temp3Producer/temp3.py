import os
import time
import random
from kafka import KafkaProducer

# Load environment variables
mean_temperature = float(os.getenv('MEAN_TEMPERATURE'))  # Mean value from environment
std_temperature = float(os.getenv('STD_TEMPERATURE'))    # Std deviation from environment
kafka_broker = os.getenv('KAFKA_BROKER')          # Kafka broker
kafka_topic = os.getenv('KAFKA_TOPIC')            # Kafka topic name

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_broker,
    value_serializer=lambda v: v.encode('utf-8')
)

def simulate_temperature(sensor_name):
    """Simulate a temperature reading for a given sensor."""
    temperature = max(0, min(100, random.gauss(mean_temperature, std_temperature)))
    timestamp = int(time.time() * 1e9)  # Nanoseconds since epoch
    return f"{sensor_name} temp3={temperature:.2f} {timestamp}"

try:
    print("Starting temperature simulation...")
    while True:
        data = simulate_temperature("sTemperature")
        producer.send(kafka_topic, data)
        print(f"Sent to Kafka: {data}")
        time.sleep(30)  # Wait for 30 seconds
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")
finally:
    producer.close()
    print("Kafka producer closed.")
