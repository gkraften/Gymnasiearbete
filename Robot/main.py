import robot.motors as motors
import robot
import robot.compass as compass
import robot.distance as distance
from vector import Vector
import vector
import time

pos = Vector(0, 0)

distance.start_measuring()
motors.forward()
time.sleep(2)
motors.stop()
after = compass.getHeading()
distance.stop_measuring()
pos += vector.from_polar(distance.get_distance(), after)

motors.right(50)
time.sleep(2)
motors.stop()

distance.start_measuring()
motors.forward()
time.sleep(2)
motors.stop()
after = compass.getHeading()
distance.stop_measuring()
pos += vector.from_polar(distance.get_distance(), after)

print("Avstånd från start: {}".format(pos.length()))