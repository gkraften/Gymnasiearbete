import RPi.GPIO as GPIO
import robot.motors
import time

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

robot.motors.forward(30)

try:
    while True:
        print(GPIO.input(7))
except:
    robot.clean()