import robot.motors
import time
import RPi.GPIO as GPIO

robot.motors.LEFT.forward()
time.sleep(1)
robot.motors.LEFT.backward()
time.sleep(1)
robot.motors.stop()
robot.motors.RIGHT.forward()
time.sleep(1)
robot.motors.RIGHT.backward()
time.sleep(1)
robot.motors.stop()
GPIO.cleanup()
