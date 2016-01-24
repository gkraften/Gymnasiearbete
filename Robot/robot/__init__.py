from subprocess import call
import RPi.GPIO as GPIO
import robot.pins as pins
import time
import math
from threading import Thread
from controller import PID

_battery_callback = None
_battery_pauses = 0
_checking_battery = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pins.BATTERY, GPIO.IN)

def _check_battery():
    global _checking_battery
    global _battery_callback

    while _checking_battery:
        try:
            if GPIO.input(pins.BATTERY) == 0:
                _battery_callback()
        except RuntimeError:
            break
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

def turn_to(heading, error=math.radians(1)):
    pid = PID(3, 0.1, 5, -50, 50)
    pid.set_target(heading)
    pid.difference = compass.angleDifference

    h = compass.getHeading()
    while abs(compass.angleDifference(h, heading)) > error:
        ret = pid.update(h)
        print(ret)
        if ret < 0:
            motors.right(50-ret)
        elif ret > 0:
            motors.left(50+ret)
        h = compass.getHeading()
        time.sleep(0.05)
    motors.stop()

def clean():
    GPIO.cleanup()
    compass.sleep()