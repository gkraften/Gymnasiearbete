from robot import compass
from robot import motors
from robot import distance
from robot import ultrasonic
import robot
import math
import vector
import time
import maplogger
import threading
import random

n = vector.Vector(0, 0)
done = False

def count():
    global n
    n += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def avsluta():
    print("Batteriet är slut!")
    robot.clean()
    robot.halt()

def supermagiskt():
    global done
    while not done:
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
        time.sleep(0.1)

try:
    maplogger.initialize()
    robot.on_battery_low(avsluta)
    compass.calibrate(5)
    robot.turn_to(math.pi/2, math.radians(4))
    input("Enter")
    logger = threading.Thread(target=supermagiskt)
    logger.start()

    distance.start_measuring(count)
    motors.forward(math.pi/2)

    while True:
        left = ultrasonic.get_left()
        middle = ultrasonic.get_middle()
        right = ultrasonic.get_right()
        print((left, middle, right))

        if left <= 15 and right <= 15:
            motors.stop()
            robot.turn_to(compass.angleDifference(compass.getHeading(), math.pi))
            motors.forward()
        elif left <= 15:
            motors.stop()
            robot.turn_to(compass.angleDifference(compass.getHeading(), math.pi/6), math.radians(4))
            motors.forward()
        elif right <= 15:
            motors.stop()
            robot.turn_to(compass.angleDifference(compass.getHeading(), -math.pi/6), math.radians(4))
            motors.forward()
        elif middle <= 15:
            motors.stop()
            robot.turn_to(compass.angleDifference(compass.getHeading(), random.choose([-1, 1])*math.pi/2))
            motors.forward
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    done = True
    distance.stop_measuring()
    motors.stop()
    logger.join()
    maplogger.close()
    robot.clean()