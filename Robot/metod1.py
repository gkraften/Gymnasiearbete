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
        u = n + vector.from_polar(m, compass.getHeading())

        l = ultrasonic.get_left()
        v = n + vector.from_polar(l, compass.getHeading() + math.radians(30))

        r = ultrasonic.get_right()
        w = n + vector.from_polar(r, compass.getHeading() - math.radians(30))

        data = []
        if m <= 400 and m >= 15:
            data.append([u.x, u.y])
        if l <= 400 and l >= 15:
            data.append([v.x, v.y])
        if r <= 400 and l >= 15:
            data.append([w.x, w.y])

        if len(data) == 0:
            maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading())
        else:
            maplogger.log(position=[[n.x, n.y]], heading=compass.getHeading(), walls=data)
        time.sleep(0.2)

try:
    maplogger.initialize("/var/www/map.txt")
    robot.on_battery_low(avsluta)
    compass.calibrate(5)
    input("Enter")
    logger = threading.Thread(target=supermagiskt)
    logger.start()

    distance.start_measuring(count)
    motors.forward()

    t = 0
    last = compass.getHeading()
    while True:
        left = ultrasonic.get_left()
        middle = ultrasonic.get_middle()
        right = ultrasonic.get_right()

        if left <= 50 and right <= 50:
            distance.stop_measuring()
            motors.stop()
            robot.turn_to(compass.getHeading() + math.pi, math.radians(10))
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()
        elif left <= 50:
            distance.stop_measuring()
            motors.stop()
            motors.right()
            time.sleep(0.5)
            motors.stop()
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()
        elif right <= 50:
            distance.stop_measuring()
            motors.stop()
            motors.left()
            time.sleep(0.5)
            motors.stop()
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()
        elif middle <= 50:
            distance.stop_measuring()
            motors.stop()
            motors.right()
            time.sleep(0.5)
            motors.stop()
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()

        if time.time() - t >= 0.5:
            if abs(compass.angleDifference(compass.getHeading(), last)) >= math.radians(10):
                distance.stop_measuring()
                motors.stop()
                done = True
                logger.join()
                a = compass.getHeading()
                compass.calibrate(3)
                done = False
                logger = threading.Thread(target=supermagiskt)
                logger.start()
                robot.turn_to(a, math.radians(13))
                time.sleep(1)
                distance.start_measuring(count)
                motors.forward()
            t = time.time()
            last = compass.getHeading()
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