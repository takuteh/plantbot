import time
import board
import adafruit_dht

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

TOKEN = "ycI8NQmPpGbA6iB-vA8Lx3wA0yaLHGV_7EKyonzFP2KwU07_EakiRZIYtbAbmqQ3h70wTkLhCrChrZCyHYZVvw=="
ORG = "takuteh"
BUCKET = "dht11"
URL = "http://localhost:8086"

client = InfluxDBClient(
    url=URL,
    token=TOKEN,
    org=ORG
)

write_api = client.write_api(write_options=SYNCHRONOUS)

dht = adafruit_dht.DHT11(board.D6)

while True:
    try:
        temp = dht.temperature
        hum = dht.humidity

        print(temp, hum)

        point = (
            Point("environment")
            .field("temperature", temp)
            .field("humidity", hum)
        )

        write_api.write(bucket=BUCKET, org=ORG, record=point)

    except Exception as e:
        print(e)

    time.sleep(10)
