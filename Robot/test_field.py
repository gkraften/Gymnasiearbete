import robot
from robot import motors
from robot import compass
import math
import time

def battery_low():
    print("Lågt batteri! Stänger av...")
    robot.clean()
    robot.halt()

robot.on_battery_low(battery_low)

compass.calibrate(10)

input("Tryck på enter för att starta")

try:
    motors.forward()
    last = compass.getHeading()
    while True:
        direction = 0#compass.getHeading()
        print(math.degrees(abs(compass.angleDifference(direction, last))))
        if math.degrees(abs(compass.angleDifference(direction, last))) > 5 and False:
            break
        last = direction
        time.sleep(1)
finally:
    motors.stop()
    robot.clean()