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
    global _meassuring
    last = 0
    while _meassuring:
        if GPIO.input(pins.HALL_EFFECT) == 0:
            dt = time.time() - last
            print(dt)
            if dt < 0.15:
                _d += HALF_CIRCUMFERENCE
                if not callback is None:
                    callback()


def start_meassuring(callback=None):
    global _meassuring
    if not _meassuring:
        _meassuring = True
        _d = 0
        t = Thread(target=_meassure, args=(callback,))
        t.start()

def stop_meassuring():
    global _meassuring
    _meassuring = False

def get_distance():
    return _d