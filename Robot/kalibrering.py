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
    robot.motors.forward(100)
    direction = compass.getHeading()
    time.sleep(1)
    new_direction = compass.getHeading()
    if compass.angleDifference(new_direction, direction) < -math.radians(0.1):
        left = True
    elif compass.angleDifference(new_direction, direction) > math.radians(0.1):
        right = True
    elif abs(compass.angleDifference(new_direction, direction)) < math.radians(0.1):
        print("Allt är perf")
        done = True


    while not done:
        if left:
            robot.motors.LEFT.forward(amount)
        elif right:
            robot.motors.RIGHT.forward(amount)
        direction = compass.getHeading()
        time.sleep(1)
        new_direction = compass.getHeading()
        if compass.angleDifference(new_direction, direction) < -math.radians(0.1):
            if left:
                amount -= 5
            elif right:
                amount += 1
        elif compass.angleDifference(new_direction, direction) > math.radians(0.1):
            if left:
                amount += 1
            elif right:
                amount -= 5
        else:
            done = True
        # grader norr från motsols
except KeyboardInterrupt:
    print("Avbryter")
finally:
    print("{} är {}".format("Höger" if right else "Vänster", amount))
    robot.clean()