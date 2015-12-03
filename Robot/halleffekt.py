import RPi.GPIO as GPIO
import robot.motors
import robot.pins as pins
import robot
import time

distance = 0

def callback(a):
    global distance
    distance += 1
    print(distance)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

robot.motors.forward(100)
try:
    while True:
        while GPIO.input(7) == 1:
            pass
        distance += 1
        print(distance)
        while GPIO.input(7) == 0:
            pass
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()