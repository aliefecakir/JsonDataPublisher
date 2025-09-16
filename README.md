# MQTT JSON Publisher

This Python script publishes random sensor data in JSON format to an MQTT broker. It simulates multiple sensors with random temperature, humidity, and status values.

## Features

* Publishes JSON data to a specific MQTT topic.
* Randomly generates:

  * `sensorId` between `sensor-1` and `sensor-5`.
  * Temperature (`25.0–50.0 °C`).
  * Humidity (`40–70 %`).
  * Pressure (`"114000-119000 pascal"`).
* Runs continuously until stopped manually (`Ctrl + C`).
* Disconnects cleanly from the MQTT broker on exit.

## Requirements

* Python 3.7+
* `paho-mqtt` library

Install `paho-mqtt` using:

```bash
python -m pip install paho-mqtt
```

## Usage

1. Make sure you have an MQTT broker running. For testing, you can use a local broker like Mosquitto:

```bash
# Linux
sudo apt install mosquitto

# macOS
brew install mosquitto

# Windows
# Download installer from https://mosquitto.org/download/
```

2. Update the script if needed:

```python
BROKER = "your-broker"          # MQTT broker address
PORT = 1883                     # Broker port
TOPIC = "your-input-topic"      # Topic to publish messages
```

3. Run the script:

```bash
python mqtt_publisher.py
```

4. Stop the script with `Ctrl + C`.

## Example Output

```
✅ Sent: {"sensorId": "sensor-3", "temperature": 46.7, "humidity": 55, "pressure": 114987}
✅ Sent: {"sensorId": "sensor-1", "temperature": 37.1, "humidity": 72, "pressure": 117728}
```

## Notes

* Modify the JSON structure in the script to include additional sensor fields or different ranges.
* This script is great for testing MQTT subscribers or dashboards.

## License

MIT License
