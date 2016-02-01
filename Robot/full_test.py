from robot import compass
from robot import motors
from robot import distance
import robot
import math
import vector
import time
import maplogger

n = vector.Vector(0, 0)

def count():
    global n
    n += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def avsluta():
    print("Batteriet är slut!")
    robot.clean()
    robot.halt()

try:
    maplogger.initialize()
    robot.on_battery_low(avsluta)
    compass.calibrate(5)
    robot.turn_to(math.pi/2, math.radians(4))
    input("Enter")

    distance.start_measuring(count)
    motors.forward(math.pi/2)
    for i in range(10):
        maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading())
        time.sleep(0.5)

finally:
    distance.stop_measuring()
    maplogger.close()
    motors.stop()
    robot.clean()