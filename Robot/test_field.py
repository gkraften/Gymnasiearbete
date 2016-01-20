import robot
from robot import motors
from robot import compass
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
        direction = compass.getHeading()
        if abs(compass.angleDifference(direction, last)) > 5:
            break
finally:
    motors.stop()
    robot.clean()