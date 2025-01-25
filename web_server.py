from flask import Flask
import RPi.GPIO as GPIO
BUTTON=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN)
#GPIO.output(26, GPIO.LOW)

app = Flask(__name__)

#Creating the Routes
@app.route("/")
def index():
	return "Hello From flask"

@app.route("/push-button")
def check_button():
	if GPIO.input(BUTTON) == GPIO.LOW:
		return "Button is pressed"
	return "Button is not pressed"

app.run(host="0.0.0.0")
