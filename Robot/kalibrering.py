import RPi.GPIO as GPIO
import robot.motors
import robot
import time
import robot.compass as compass
import robot.distance
import math

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

left = 100
right = 100
direction = 0
new_direction = 0

done = True

def wheel_turned():
    global done
    done = False

try:
    robot.motors.forward(100)
    robot.distance.start_meassuring(wheel_turned)
    while done:
        pass
    robot.distance.stop_meassuring()
    while not done:
        robot.motors.LEFT.forward(left)
        robot.motors.RIGHT.forward(right)
        direction = compass.getHeading()
        time.sleep(1)
        new_direction = compass.getHeading()
        if compass.angleDifference(new_direction, direction) < -math.radians(0.1):
            left -= 5
        elif compass.angleDifference(new_direction, direction) > math.radians(0.1):
            right -= 5
        elif abs(compass.angleDifference(new_direction, direction)) < math.radians(0.1):
            done = True
        # grader norr från motsols
except KeyboardInterrupt:
    pass
finally:
    if done:
        print("Höger kör {}\tVänster kör {}".format(right, left))
    robot.clean()