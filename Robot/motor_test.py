import robot.motors as motors
import time
import RPi.GPIO as GPIO

motors.forward()
time.sleep(2)
motors.forward(50)
time.sleep(2)
motors.stop()
time.sleep(3)

GPIO.cleanup()