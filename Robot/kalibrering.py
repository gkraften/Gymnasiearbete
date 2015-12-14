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

motor = None
angle = 0

try:
    robot.motors.forward(100)
    direction = compass.getHeading()
    time.sleep(1)
    new_direction = compass.getHeading()
    if compass.angleDifference(new_direction, direction) < -math.radians(0.1):
        motor = robot.motors.LEFT
        angle = -1
    elif compass.angleDifference(new_direction, direction) > math.radians(0.1):
        motor = robot.motors.RIGHT
        angle = 1
    elif abs(compass.angleDifference(new_direction, direction)) < math.radians(0.1):
        print("Allt är perf")
        done = True


    while not done:
        motor.forward(amount)
        direction = compass.getHeading()
        time.sleep(0.75)
        new_direction = compass.getHeading()
        if compass.angleDifference(new_direction, direction) < angle*math.radians(0.1):
            amount -= 7
        elif compass.angleDifference(new_direction, direction) > -angle*math.radians(0.1):
            amount += 1
        elif abs(compass.angleDifference(new_direction, direction)) < math.radians(0.1):
            done = True
        # grader norr från motsols
except KeyboardInterrupt:
    print("Avbryter")
finally:
    print("{} är {}".format("Höger" if angle == 1 else "Vänster", amount))
    robot.clean()