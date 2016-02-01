from robot import compass
from robot import motors
from robot import distance
from robot import ultrasonic
import robot
import math
import vector
import time
import maplogger

n = vector.Vector(0, 0)

def count():
    global n
    n += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def avsluta():
    print("Batteriet är slut!")
    robot.clean()
    robot.halt()

try:
    maplogger.initialize()
    robot.on_battery_low(avsluta)
    compass.calibrate(5)
    robot.turn_to(math.pi/2, math.radians(4))
    input("Enter")

    distance.start_measuring(count)
    motors.forward(math.pi/2)
    for i in range(10):
        m = ultrasonic.get_middle()
        u = vector.from_polar(m, compass.getHeading())

        l = ultrasonic.get_left()
        v = vector.from_polar(l, compass.angleDifference(compass.getHeading(), -math.radians(30)))

        r = ultrasonic.get_right()
        w = vector.from_polar(r, compass.angleDifference(compass.getHeading(), math.radians(30)))

        data = []
        if m <= 400:
            data.append([u.x, u.y])
        if l <= 400:
            data.append([v.x, v.y])
        if r <= 400:
            data.append([w.x, w.y])

        if len(data) == 0:
            maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading())
        else:
            maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading(), walls=data)
        time.sleep(0.5)
    motors.stop()
    distance.stop_measuring()
    robot.turn_to(0, math.radians(4))
    motors.forward(0)
    for i in range(6):
        m = ultrasonic.get_middle()
        u = vector.from_polar(m, compass.getHeading())

        l = ultrasonic.get_left()
        v = vector.from_polar(l, compass.angleDifference(compass.getHeading(), -math.radians(30)))

        r = ultrasonic.get_right()
        w = vector.from_polar(r, compass.angleDifference(compass.getHeading(), math.radians(30)))

        data = []
        if m <= 400:
            data.append([u.x, u.y])
        if l <= 400:
            data.append([v.x, v.y])
        if r <= 400:
            data.append([w.x, w.y])

        if len(data) == 0:
            maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading())
        else:
            maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading(), walls=data)
        time.sleep(0.5)

finally:
    distance.stop_measuring()
    maplogger.close()
    motors.stop()
    robot.clean()