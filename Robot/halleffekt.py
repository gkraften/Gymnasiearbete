import RPi.GPIO as GPIO
import robot.motors
import robot
import random

distance = 0

def callback(a):
    global distance
    distance += 1

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(7, GPIO.FALLING, callback=callback)

robot.motors.LEFT.forward(30)
try:
    while True:
        while GPIO.input(7) == 1:
            pass
        while GPIO.input(7) == 0:
            pass
        if GPIO.input(7) == 1:
            print(random.random())
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()