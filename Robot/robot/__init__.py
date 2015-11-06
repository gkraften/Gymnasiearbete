from subprocess import call
import RPi.GPIO as GPIO
import robot.pins as pins

def is_battery_low():
    return not GPIO.input(pins.BATTERY)

def halt():
    call(["halt"])