import robot.motors
import robot.distance
import robot
import random
import time
import RPi.GPIO as GPIO

robot.on_battery_low(lambda: print("Lågt batteri!"))

robot.motors.forward()

try:
    while True:
        if robot.distance.get_mid() < 30:
            random.choice([robot.motors.left, robot.motors.right])()
            time.sleep(0.1)
            robot.forward()
        time.sleep(0.1)
finally:
    GPIO.cleanup()