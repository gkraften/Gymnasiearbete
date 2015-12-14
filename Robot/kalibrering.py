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

amount = 100
direction = 0
new_direction = 0
done = False

left = False
right = False

try:
    robot.motors.RIGHT.forward(100)
    while not done:
        robot.motors.LEFT.forward(amount)
        direction = compass.getHeading()
        time.sleep(1)
        new_direction = compass.getHeading()
        if compass.angleDifference(new_direction, direction) < -math.radians(1):
            amount -= 5
        elif compass.angleDifference(new_direction, direction) > math.radians(1):
            amount += 1
        else:
            done = True
        # grader norr från motsols
except KeyboardInterrupt:
    print("Avbryter")
finally:
    print("{} är {}".format("Höger" if right else "Vänster", amount))
    robot.clean()