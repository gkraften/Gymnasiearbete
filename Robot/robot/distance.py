import RPi.GPIO as GPIO
import robot.pins as pins
from threading import Thread
import time

GPIO.setup(pins.HALL_EFFECT, GPIO.IN)

_measuring = False
_d = 0

HALF_CIRCUMFERENCE = 10.21

def _measure(callback):
    global _d
    global _measuring
    last = 0
    while _measuring:
        #try:
        if GPIO.input(pins.HALL_EFFECT) == 0:
            dt = time.time() - last
            if dt > 0.15:
                last = time.time()
                _d += HALF_CIRCUMFERENCE
                if not callback is None:
                    callback()
        #except RuntimeError:
        #    break
    print("DÖDAA")


def start_measuring(callback=None):
    global _measuring
    if not _measuring:
        _measuring = True
        _d = 0
        t = Thread(target=_measure, args=(callback,))
        t.start()

def stop_measuring():
    global _measuring
    _measuring = False

def get_distance():
    return _d