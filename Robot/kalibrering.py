import RPi.GPIO as GPIO
import robot.motors
import robot
import time
import robot.compass as compass
import robot.distance
import math

def low_battery():
    print("Lågt batteri!")
    robot.halt()

robot.on_battery_low(low_battery)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

left = 100
right = 100
direction = 0
new_direction = 0

try:
    while True:
        robot.motors.LEFT.forward(left)
        robot.motors.RIGHT.forward(right)
        direction = compass.getHeading()
        time.sleep(0.75)
        new_direction = compass.getHeading()
        if compass.angleDifference(new_direction, direction) < -math.radians(0.1):
            left -= 2
            print("Vänster", left)

        elif compass.angleDifference(new_direction, direction) > math.radians(0.1):
            right -= 2
            print("Höger:", right)

        elif abs(compass.angleDifference(new_direction, direction)) < math.radians(0.1):
            break
        # grader norr från motsols
except KeyboardInterrupt:
    print("Avbryter")
finally:
    print("Höger kör {}\tVänster kör {}".format(right, left))
    robot.clean()