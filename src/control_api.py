from flask import Flask
import os

app = Flask(__name__)

@app.route("/pump/on")
def pump_on():
    os.system("python3 /home/pi/plantbot/src/pump_on.py")
    return "pump on"

@app.route("/pump/off")
def pump_off():
    os.system("python3 /home/pi/plantbot/src/pump_off.py")
    return "pump off"

app.run(host="0.0.0.0", port=5000)
