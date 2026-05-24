import RPi.GPIO as GPIO
import time
from influxdb_client import InfluxDBClient, Point

PIN = 26

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

# InfluxDB設定
client = InfluxDBClient(
    url="http://localhost:8086",
    token="ycI8NQmPpGbA6iB-vA8Lx3wA0yaLHGV_7EKyonzFP2KwU07_EakiRZIYtbAbmqQ3h70wTkLhCrChrZCyHYZVvw==",
    org="takuteh"
)

write_api = client.write_api()

BUCKET = "soil_humidity"
THRESHOLD_STATUS = 0  # 今はデジタルなので0/1扱い

try:
    while True:
        raw = GPIO.input(PIN)

        # 君のセンサーは
        # 0 = 水あり
        # 1 = 水なし
        if raw == 0:
            status = 1  # 水あり
            text = "水あり"
        else:
            status = 0  # 水なし
            text = "水なし"

        print(text)

        point = (
            Point("soil")
            .field("status", status)
        )

        write_api.write(
            bucket=BUCKET,
            org="takuteh",
            record=point
        )

        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
