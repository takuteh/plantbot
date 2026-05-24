import RPi.GPIO as GPIO
import time
import requests
import os
from datetime import datetime

WEBHOOK_URL = "https://hooks.slack.com/services/~"

RELAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

# 保存先
SAVE_DIR = "/home/pi/images"
os.makedirs(SAVE_DIR, exist_ok=True)

try:
    # 散水ON
    GPIO.output(RELAY, GPIO.HIGH)

    # 水が出るまで少し待つ
    time.sleep(5)

    # snapshot取得
    url = "http://127.0.0.1:8080/?action=snapshot"

    r = requests.get(url)

    # ファイル名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{SAVE_DIR}/{timestamp}.jpg"

    # 保存
    with open(filename, "wb") as f:
        f.write(r.content)

    print(f"saved: {filename}")

    # Slack通知
    requests.post(
        WEBHOOK_URL,
        json={
            "text": f"散水しました\n画像保存: {filename}"
        }
    )

    # さらに散水
    time.sleep(10)

finally:
    # 散水OFF
    GPIO.output(RELAY, GPIO.LOW)
    GPIO.cleanup()
