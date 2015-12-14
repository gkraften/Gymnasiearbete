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

motors.forward()
time.sleep(2)
motors.stop()
pos += vector.from_polar(25.22*2, compass.getHeading())

motors.right(50)
time.sleep(1)
motors.stop()

motors.forward()
time.sleep(2)
motors.stop()
pos += vector.from_polar(25.22*2, compass.getHeading())

print(pos.length())
robot.clean()