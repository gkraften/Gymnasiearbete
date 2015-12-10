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

done = True
try:
    while done:
        robot.motors.LEFT.forward(left)
        robot.motors.RIGHT.forward(right)
        direction = compass.getHeading
        time.sleep(0.5)
        new_direction = compass.getHeading
        if direction - new_direction > 0:
            right -= 5
        if direction - new_direction < 0:
            left -= 5
        if direction - new_direction == 0:
            done = False
        # grader norr från motsols
except KeyboardInterrupt:
    print("Höger kör", right, "Vänster kör", left)
finally:
    robot.clean()