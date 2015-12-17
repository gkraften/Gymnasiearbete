import RPi.GPIO as GPIO
import robot.pins as pins
from threading import Thread
import time

GPIO.setup(pins.HALL_EFFECT, GPIO.IN)

_measuring = False
_d = 0
_thread = None

HALF_CIRCUMFERENCE = 10.21

def _measure(callback):
    global _d
    global _measuring
    last = 0
    while _measuring:
        #try:
        if GPIO.input(pins.HALL_EFFECT) == 0:
            dt = time.time() - last
            if dt > 0.25:
                last = time.time()
                _d += HALF_CIRCUMFERENCE
                if not callback is None:
                    callback()
        #except RuntimeError:
        #    break


def start_measuring(callback=None):
    global _measuring
    global _thread
    if not _measuring:
        _measuring = True
        _d = 0
        _thread = Thread(target=_measure, args=(callback,))
        _thread.start()

def stop_measuring():
    global _measuring
    global _thread
    _measuring = False
    _thread.join()

def get_distance():
    return _d