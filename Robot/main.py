import robot.motors as motors
import robot
import robot.compass as compass
import robot.distance as distance
from vector import Vector
import vector
import time
import sys

robot.on_battery_low(robot.halt)

pos = Vector(0, 0)

def f():
    global pos
    pos += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

distance.start_measuring(f)
motors.forward()
time.sleep(2)
motors.stop()
distance.stop_measuring()

motors.right(50)
time.sleep(2)
motors.stop()

distance.start_measuring(f)
motors.forward()
time.sleep(2)
motors.stop()
distance.stop_measuring()

print(pos.length())
robot.clean()