import RPi.GPIO as GPIO
import robot.pins as pins
from threading import Thread
import time

GPIO.setup(pins.HALL_EFFECT, GPIO.IN)

_meassuring = False
_d = 0

HALF_CIRCUMFERENCE = 10.21

def _meassure(callback):
    global _d
    last = 0
    while _meassuring:
        if GPIO.input(pins.HALL_EFFECT) == 0:
            dt = time.time() - last
            if dt < 0.15:
                _d += HALF_CIRCUMFERENCE
                if not callback is None:
                    callback()


def start_meassuring(callback=None):
    if not _meassuring:
        _meassuring = True
        t = Thread(target=_meassure, args=(callback,))
        t.start()

def stop_meassuring():
    _meassuring = False
    _d = 0

def get_distance():
    return _d