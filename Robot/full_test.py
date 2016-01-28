from robot import compass
from robot import motors
from robot import distance
import robot
import math
import vector
import time

n = vector.Vector(0, 0)

def count():
    global n
    n += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def avsluta():
    print("Batteriet är slut!")
    robot.clean()
    robot.halt()

try:
    robot.on_battery_low(avsluta)
    compass.calibrate(5)
    robot.turn_to(math.pi/2, math.radians(4))
    input("Enter")
    distance.start_measuring(count)
    motors.forward(math.pi/2)
    time.sleep(3)
    motors.stop()
    distance.stop_measuring()
    robot.turn_to(0)
    distance.start_measuring(count)
    motors.forward()
    time.sleep(1)
    motors.stop()
    distance.stop_measuring()
    print("{}cm".format(n.length()))
finally:
    motors.stop()
    robot.clean()