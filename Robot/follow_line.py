from robot import compass
from robot import motors
from robot import distance
import robot
import vector
from line import Line
import math
import time

l = Line(vector.Vector(0, 0), vector.from_polar(1, math.radians(135)))
p = vector.Vector(0, 0)

def pos():
    global p
    p += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def avsluta():
    print("Batteriet är slut!")
    robot.clean()
    robot.halt()

robot.on_battery_low(avsluta)
compass.calibrate(5)
robot.turn_to(l.direction.angle())
input("Tryck på enter ")

try:
    distance.start_measuring(pos)
    while True:
        if l.distance_to(p) < 10:
            motors.forward(l.direction.angle())
        else:
            if compass.angleDifference(p.angle(), l.direction.angle()) > 0:
                motors.forward(0)
            else:
                motors.forward(math.pi)
        time.sleep(0.1)
finally:
    motors.stop()
    distance.stop_measuring()
    robot.clean()