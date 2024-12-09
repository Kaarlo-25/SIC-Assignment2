import os
import time
import random
from kafka import KafkaProducer

# Load environment variables
mean_cooling = float(os.getenv('MEAN_COOLING'))  # Mean value from environment
std_cooling = float(os.getenv('STD_COOLING'))    # Std deviation from environment
kafka_broker = os.getenv('KAFKA_BROKER')          # Kafka broker
kafka_topic = os.getenv('KAFKA_TOPIC')            # Kafka topic name

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_broker,
    value_serializer=lambda v: v.encode('utf-8')
)

def simulate_cooling(sensor_name):
    """Simulate a cooling reading for a given sensor."""
    cooling = max(5, min(20, random.gauss(mean_cooling, std_cooling)))
    timestamp = int(time.time() * 1e9)  # Nanoseconds since epoch
    return f"{sensor_name} cooling={cooling:.2f} {timestamp}"

try:
    print("Starting cooling simulation...")
    while True:
        data = simulate_cooling("sCooling")
        producer.send(kafka_topic, data)
        print(f"Sent to Kafka: {data}")
        time.sleep(60)  # Wait for 60 seconds
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")
finally:
    producer.close()
    print("Kafka producer closed.")
