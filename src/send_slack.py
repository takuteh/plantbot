import requests
from slack_sdk import WebClient

TOKEN = "xoxb"
CHANNEL = ""

# mjpg-streamerから静止画取得
url = "http://localhost:8080/?action=snapshot"

img = requests.get(url)

with open("image.jpg", "wb") as f:
    f.write(img.content)

# Slack送信
client = WebClient(token=TOKEN)

client.files_upload_v2(
    channel=CHANNEL,
    file="image.jpg",
    title="散水しました",
    initial_comment="散水しました"
)

print("送信完了")
