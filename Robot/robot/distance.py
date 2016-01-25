import RPi.GPIO as GPIO
import robot.pins as pins
from threading import Thread
import time

_measuring = False
_d = 0
_thread = None

HALF_CIRCUMFERENCE = 10.21

GPIO.setup(pins.HALL_EFFECT, GPIO.IN)

def _measure(callback):
    global _measuring
    last = 1
    while _measuring:
        now = GPIO.input(pins.HALL_EFFECT)
        if now == 0 and last == 1:
            callback()
        last = now

def start_measuring(callback):
    global _measuring
    global _d
    if not _measuring:
        _measuring = True
        _d = 0
        Thread(target=_measure, args=(callback))

def stop_measuring():
    global _measuring
    _measuring = False

def get_distance():
    return _d