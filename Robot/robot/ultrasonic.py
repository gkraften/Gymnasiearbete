import robot.pins as pins
import RPi.GPIO as GPIO
import time
from threading import Lock

class Rangefinder:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        self.lock = Lock()
        self.last = 0
        self.last_distance = 0

        GPIO.setup(trig, GPIO.OUT, initial=False)
        GPIO.setup(echo, GPIO.IN)

    def distance(self):
        self.lock.acquire()
        while time.time() - self.last < 0.05:
            self.lock.release()
            return self.last_distance
        self.last = time.time()
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0:
            pass
        start = time.time()

        while GPIO.input(self.echo) == 1:
            pass

        stop = time.time()

        d = (stop - start) * 17150
        self.last_distance = d

        self.lock.release()
        return d

_LEFT = Rangefinder(pins.DISTANCE_LEFT_TRIG, pins.DISTANCE_LEFT_ECHO)
_MIDDLE = Rangefinder(pins.DISTANCE_MID_TRIG, pins.DISTANCE_MID_ECHO)
_RIGHT = Rangefinder(pins.DISTANCE_RIGHT_TRIG, pins.DISTANCE_RIGHT_ECHO)

def get_middle():
    return _MIDDLE.distance() + 14

def get_right():
    return _RIGHT.distance() + 14

def get_left():
    return _LEFT.distance() +  14