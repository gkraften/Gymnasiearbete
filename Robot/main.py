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
d = 0

def f():
    global pos
    global d
    d += 1
    pos += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

distance.start_measuring(f)
motors.forward()
time.sleep(5)
motors.stop()
distance.stop_measuring()

print(pos.length())
print(d)
robot.clean()