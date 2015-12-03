import RPi.GPIO as GPIO
import robot.motors
import time

distance = 0

def callback(a):
    global distance
    distance += 10.21
    print(distance)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(7, GPIO.FALLING, callback=callback, bouncetime=50)

a = False
robot.motors.forward(30)
try:
    while True:
        if GPIO.input(7) == 0 and a:
            a = False
            distance += 1
            print(distance)
        else:
            if GPIO.input(7) == 1:
                a = True
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()