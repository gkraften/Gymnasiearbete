# Programmet ser ständigt efter om batteriet håller på
# att ta slut och stänger i så fall av datorn.

import robot
import time
import RPi.GPIO as GPIO

while True:
    if robot.is_battery_low():
        with open("/home/pi/Desktop/halt.txt", "w") as f:
            print("Batteriet är lågt! Stänger av.", file=f)
        GPIO.cleanup()
        robot.halt()
    time.sleep(1)