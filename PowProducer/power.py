import os
import time
import random
from kafka import KafkaProducer

# Load environment variables
mean_power = float(os.getenv('MEAN_POWER'))  # Mean value from environment
std_power = float(os.getenv('STD_POWER'))    # Std deviation from environment
kafka_broker = os.getenv('KAFKA_BROKER')          # Kafka broker
kafka_topic = os.getenv('KAFKA_TOPIC')            # Kafka topic name

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_broker,
    value_serializer=lambda v: v.encode('utf-8')
)

def simulate_power(sensor_name):
    """Simulate a power reading for a given sensor."""
    power = max(100, min(2000, random.gauss(mean_power, std_power)))
    timestamp = int(time.time() * 1e9)  # Nanoseconds since epoch
    return f"{sensor_name} power={power:.2f} {timestamp}"

try:
    print("Starting power simulation...")
    while True:
        data = simulate_power("sPower")
        producer.send(kafka_topic, data)
        print(f"Sent to Kafka: {data}")
        time.sleep(20)  # Wait for 20 seconds
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")
finally:
    producer.close()
    print("Kafka producer closed.")
