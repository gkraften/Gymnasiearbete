import robot.motors as motors
import robot
import robot.compass as compass
import robot.distance as distance
from vector import Vector
import vector
import time
import sys

robot.on_battery_low(robot.halt)

t = time.time()
motors.forward()

try:
    while True:
        pass
except KeyboardInterrupt:
    robot.clean()
    print(25.22*(time.time() - t))