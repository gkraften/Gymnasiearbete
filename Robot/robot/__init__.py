from subprocess import call
import RPi.GPIO as GPIO
import pins

def is_battery_low():
    return GPIO.input(pins.BATTERY)

def halt():
    call(["halt"])