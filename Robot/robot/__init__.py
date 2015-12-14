from subprocess import call
import RPi.GPIO as GPIO
import robot.pins as pins
import time
import math
from threading import Thread

_battery_callback = None
_battery_pauses = 0
_checking_battery = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pins.BATTERY, GPIO.IN)

def _check_battery():
    global _checking_battery
    global _battery_callback

    while _checking_battery:
        if GPIO.input(pins.BATTERY) == 0:
            _battery_callback()
        time.sleep(1)

def on_battery_low(callback):
    global _battery_callback
    global _checking_battery

    _battery_callback = callback
    if _battery_pauses == 0 and not _checking_battery:
        resume_battery_detection()


def pause_battery_detection():
    global _battery_pauses
    global _checking_battery

    _checking_battery = False
    _battery_pauses += 1

def resume_battery_detection():
    global _battery_pauses
    global _checking_battery

    if _battery_pauses > 0:
        _battery_pauses -= 1
    if not _battery_callback is None and _battery_pauses == 0:
        _checking_battery = True
        t = Thread(target=_check_battery)
        t.start()

def halt():
    call(["halt"])


import robot.compass as compass
import robot.motors as motors

def turn_to(heading, error=math.radians(1), speed=80):
    tries = 0
    while abs(compass.angleDifference(compass.getHeading(), heading)) > error:
        tries += 1
        while abs(compass.angleDifference(compass.getHeading(), heading)) > error:
            if compass.angleDifference(heading, compass.getHeading()) > 0:
                motors.left(speed)
            else:
                motors.right(speed)
        motors.stop()
        time.sleep(1)
        if tries == 3:
            tries = 0
            motors.left(50)
            time.sleep(1)

def clean():
    GPIO.cleanup()
    compass.sleep()