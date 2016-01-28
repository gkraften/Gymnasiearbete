from robot import compass
from robot import motors
from robot import range
import robot
import vector
import time
import math
from subprocess import call

call(["service", "apache2", "start"])

f = open("/var/www/map.txt", "w")

try:
    compass.calibrate(5)
    motors.left(60)
    turns = -1
    start = compass.getHeading()
    while turns < 2:
        u = vector.from_polar(range.MIDDLE.distance(), compass.getHeading())
        print("{},{}".format(u.x, u.y), file=f)

        v = vector.from_polar(range.LEFT.distance(), compass.angleDifference(compass.getHeading(), -math.pi/4))
        print("{},{}".format(v.x, v.y), file=f)

        w = vector.from_polar(range.RIGHT.distance(), compass.angleDifference(compass.getHeading(), math.pi/4))
        print("{},{}".format(w.x, w.y), file=f)

        dtheta = compass.angleDifference(compass.getHeading(), start)
        if dtheta > math.pi/4 and dtheta < math.pi:
            turns += 1

        time.sleep(0.1)
finally:
    motors.stop()
    robot.clean()
    f.close()