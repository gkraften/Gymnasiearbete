import robot.motors as motors
import time
import RPi.GPIO as GPIO

motors.left()
time.sleep(2)

GPIO.cleanup()