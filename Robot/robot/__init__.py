from subprocess import call
import RPi.GPIO as GPIO
import robot.pins as pins

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pins.BATTERY)

def on_battery_low(callback):
    GPIO.remove_event_detect(pins.BATTERY)
    GPIO.add_event_detect(pins.BATTERY, GPIO.FALLING, callback=callback, bouncetime=300)

def halt():
    call(["halt"])