import robot.motors
import time
import RPi.GPIO as GPIO

try:
    robot.motors.LEFT.forward()
    robot.motors.RIGHT.forward()
    while True:
        pass
finally:
    GPIO.cleanup()