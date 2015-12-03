import RPi.GPIO as GPIO
#import robot.motors
import robot.pins as pins
import time

distance = 0

def callback(a):
    global distance
    distance += 1
    print(distance)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(7, GPIO.FALLING, callback=callback, bouncetime=100)

GPIO.setup(pins.MOTOR_LEFT_1, GPIO.OUT)
GPIO.setup(pins.MOTOR_LEFT_2, GPIO.OUT)
GPIO.output(pins.MOTOR_LEFT_1, 1)
try:
    while True:
        GPIO.wait_for_edge(7, GPIO.FALLING)
        distance += 1
        if (distance == 3):
            print(distance)
            break
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()