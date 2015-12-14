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

distance.start_measuring()
motors.forward()
time.sleep(2)
motors.stop()
distance.stop_measuring()
pos += vector.from_polar(distance.get_distance(), compass.getHeading())

motors.right(50)
time.sleep(1)
motors.stop()

distance.start_measuring()
motors.forward()
time.sleep(2)
motors.stop()
distance.stop_measuring()
pos += vector.from_polar(distance.get_distance(), compass.getHeading())

print(pos.length())
robot.clean()