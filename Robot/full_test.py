from robot import compass
from robot import motors
from robot import distance
import robot
import math
import vector
import time

n = vector.Vector(0, 0)
testa = True

def count():
    global n
    n += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def magnetic_field():
    global testa
    last = compass.getHeading()
    while testa:
        now = compass.getHeading()
        dtheta = abs(compass.angleDifference(now, last))
        if dtheta > 10 and motors.current_direction == motors.DIRECTION_FORWARD:


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
    t = time.time()
    last = compass.getHeading()
    while time.time() - t < 6:
        now = compass.getHeading()
        dtheta = abs(compass.angleDifference(now, last))
        if dtheta > 10:
            compass.calibrate(5)
        time.sleep(0.1)
    motors.stop()
    distance.stop_measuring()

    robot.turn_to(0, math.radians(4))
    distance.start_measuring(count)
    motors.forward(0)
    t = time.time()
    last = compass.getHeading()
    while time.time() - t < 3:
        now = compass.getHeading()
        dtheta = abs(compass.angleDifference(now, last))
        if dtheta > 10:
            compass.calibrate(5)
        time.sleep(0.1)
    motors.stop()
    distance.stop_measuring()
    compass.calibrate(5)

    robot.turn_to(math.pi, math.radians(4))
    distance.start_measuring(count)
    motors.forward(math.pi)
    t = time.time()
    last = compass.getHeading()
    while time.time() - t < 3:
        now = compass.getHeading()
        dtheta = abs(compass.angleDifference(now, last))
        if dtheta > 10:
            compass.calibrate(5)
        time.sleep(0.1)
    motors.stop()
    distance.stop_measuring()

    print("{}cm".format(n.length()))
finally:
    motors.stop()
    robot.clean()