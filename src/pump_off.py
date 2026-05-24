import RPi.GPIO as GPIO

RERAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RERAY, GPIO.OUT)

GPIO.output(RERAY, GPIO.LOW)

GPIO.cleanup()
