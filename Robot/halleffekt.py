import RPi.GPIO as GPIO
import robot.motors
import time

distance = 0

def callback(a):
    global distance
    distance += 1
    print(distance)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(7, GPIO.FALLING, callback=callback, bouncetime=100)

robot.motors.forward(30)
try:
    while True:
        while GPIO.input(7) == 1:
            pass
        if GPIO.input(7) == 0:
            distance += 1
            while GPIO.input(7) == 0:
                pass
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()