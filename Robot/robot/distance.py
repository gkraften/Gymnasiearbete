import RPi.GPIO as GPIO
import robot.pins as pins
from threading import Thread

GPIO.setup(pins.HALL_EFFECT, GPIO.IN)