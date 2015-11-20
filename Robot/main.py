import robot.motors
import robot.distance
import robot
import random
import time
import RPi.GPIO as GPIO

robot.on_battery_low(lambda: print("Lågt batteri!"))

#robot.motors.forward()

try:
    while True:
        print("Vänster: " + robot.distance.get_left())
        print("Mitten: " + robot.distance.get_mid())
        print("Höger: " + robot.distance.get_right())
        time.sleep(0.1)
finally:
    GPIO.cleanup()