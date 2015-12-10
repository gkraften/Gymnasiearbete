import RPi.GPIO as GPIO
import robot.motors
import robot
import time

distance = 0

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

robot.motors.LEFT.forward(80)
robot.motors.RIGHT.forward(100)
try:
    last = 0
    while True:
       if GPIO.input(7) == 0:
            dt = time.time() - last
            if (dt > 0.15):
                last = time.time()
                distance += 10.21
except KeyboardInterrupt:
    print(distance)
finally:
    robot.clean()