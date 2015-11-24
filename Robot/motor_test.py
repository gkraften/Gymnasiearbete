import robot.motors as motors
import time
import RPi.GPIO as GPIO

motors.left(50)
time.sleep(2)

GPIO.cleanup()