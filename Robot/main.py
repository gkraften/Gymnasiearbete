import robot.motors as motors
import robot
import robot.compass as compass
import robot.distance as distance
from vector import Vector
import vector
import time
import sys

robot.on_battery_low(robot.halt)

distance.start_measuring()
motors.forward()

try:
    while True:
        pass
except KeyboardInterrupt:
    distance.stop_measuring()
    print(distance.get_distance() - distance.HALF_CIRCUMFERENCE)
    robot.clean()