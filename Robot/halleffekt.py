import RPi.GPIO as GPIO
import robot.motors
import time

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

robot.motors.forward(50)
distance = 0
try:
    while True:
        if GPIO.input(7) == 0:
            distance += 10.21
        while GPIO.input(7) == 0:
            pass
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()