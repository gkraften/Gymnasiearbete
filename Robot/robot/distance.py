import RPi.GPIO as GPIO
import robot.pins as pins
from threading import Thread
import time

_measuring = False
_d = 0
_thread = None
_callback = None

HALF_CIRCUMFERENCE = 10.21

GPIO.setup(pins.HALL_EFFECT, GPIO.IN)

def _measure():
    global _measuring
    global _callback
    last = []
    for i in range(100):
        last.append(1)
    while _measuring:
        now = GPIO.input(pins.HALL_EFFECT)

        if now == 0:
            all_ones = True
            for i in last:
                if i == 0:
                    all_ones = False
                    break
            if all_ones:
                _callback()

        for i in range(99, 0):
            last[i] = last[i - 1]
        last[0] = now

def start_measuring(callback):
    global _measuring
    global _d
    global _callback
    if not _measuring:
        _measuring = True
        _d = 0
        _callback = callback
        Thread(target=_measure).start()

def stop_measuring():
    global _measuring
    _measuring = False

def get_distance():
    return _d