import RPi.GPIO as GPIO
import robot.motors
import robot
import random
import time

distance = 0

def callback(a):
    global distance
    distance += 1

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(7, GPIO.FALLING, callback=callback)

robot.motors.LEFT.forward(100)
try:
    last = 0
    while True:
       if GPIO.input(7) == 0:
            dt = time.time() - last
            if (dt > 0.3):
                last = time.time()
                distance += 1
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()