import robot.pins as pins
import RPi.GPIO as GPIO
import time

class Rangefinder:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

        GPIO.setup(trig, GPIO.OUT, initial=False)
        GPIO.setup(echo, GPIO.IN)

    def distance(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0:
            pass
        start = time.time()

        while GPIO.input(self.echo) == 1:
            pass

        stop = time.time()

        return (stop - start) * 17150

LEFT = Rangefinder(pins.DISTANCE_LEFT_TRIG, pins.DISTANCE_LEFT_ECHO)
MIDDLE = Rangefinder(pins.DISTANCE_MID_TRIG, pins.DISTANCE_MID_ECHO)
RIGHT = Rangefinder(pins.DISTANCE_RIGHT_TRIG, pins.DISTANCE_RIGHT_ECHO)