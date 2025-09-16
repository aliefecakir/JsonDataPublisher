import random
import json
import time
import paho.mqtt.client as mqtt

BROKER = "your-broker"
PORT = 1883
TOPIC = "ypur-input-topic"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

try:
    while True:
        sensor_id = f"sensor-{random.randint(1, 5)}"
        data = {"sensorId": sensor_id,
                "temperature": round(random.uniform(25.0, 50.0), 1),
                "humidity": random.randint(50, 80),
                "pressure": random.randint(114000, 119000)
                }

        payload = json.dumps(data)
        result = client.publish(TOPIC, payload)

        if result[0] == 0:
            print(f"Sent: {payload}")
        else:
            print(f"Failed to send: {payload}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping publisher...")
    client.disconnect()
