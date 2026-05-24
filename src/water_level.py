import RPi.GPIO as GPIO
import time
from influxdb_client import InfluxDBClient, Point

pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# InfluxDB設定
client = InfluxDBClient(
    url="http://localhost:8086",
    token="ycI8NQmPpGbA6iB-vA8Lx3wA0yaLHGV_7EKyonzFP2KwU07_EakiRZIYtbAbmqQ3h70wTkLhCrChrZCyHYZVvw==",
    org="takuteh"
)

write_api = client.write_api()
BUCKET = "water_tank"

while True:
    raw = GPIO.input(pin)

    if raw == 0:
        print("水なし（OFF）")
        status = 0
    else:
        print("水あり（ON）")
        status = 1

    point = (
        Point("water_tank")
        .field("status", status)
    )

    write_api.write(
        bucket=BUCKET,
        org="takuteh",
        record=point
    )

    time.sleep(5)
