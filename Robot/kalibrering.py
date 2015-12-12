import RPi.GPIO as GPIO
import robot.motors
import robot
import time
import robot.compass as compass

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
        time.sleep(0.5)
        new_direction = compass.getHeading()
        if compass.angleDifference(new_direction, direction) < -0.5:
            left -= 5
        elif compass.angleDifference(new_direction, direction) > 0.5:
            right -= 5
        elif abs(compass.angleDifference(new_direction, direction)) < 0.5:
            break
        # grader norr från motsols
except KeyboardInterrupt:
    print("Höger kör {}\tVänster kör {}".format(right, left))
finally:
    robot.clean()