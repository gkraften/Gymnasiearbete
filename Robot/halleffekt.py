import RPi.GPIO as GPIO
import robot.motors
import time

distance = 0

def callback(a):
    global distance
    distance += 10.21
    print(distance)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(7, GPIO.FALLING, callback=callback, bouncetime=200)

robot.motors.forward(20)
try:
    while True:
        while GPIO.input(7) == 1:
            pass
        print(GPIO.input(7))
        while GPIO.input(7) == 0:
            pass
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()