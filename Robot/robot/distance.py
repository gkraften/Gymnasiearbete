import robot.pins as pins
import RPi.GPIO as GPIO
import time

GPIO.setup(pins.DISTANCE_MID_TRIG, GPIO.OUT)
GPIO.setup(pins.DISTANCE_MID_ECHO, GPIO.IN)

def get(trig, echo):
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

    while GPIO.input(echo) == 0:
        pass
    start = time.time()

    while GPIO.input(echo) == 1:
        pass

    stop = time.time()

    return (stop - start) * 17150

def get_mid():
    return get(pins.DISTANCE_MID_TRIG, pins.DISTANCE_MID_ECHO)