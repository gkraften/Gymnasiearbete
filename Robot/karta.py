from robot import compass
from robot import motors
from robot import ultrasonic
import robot
import vector
import time
import math
from subprocess import call
import maplogger

maplogger.initialize("/var/www/map.txt")

try:
    compass.calibrate(5)
    input("Tryck på enter för att starta\n")
    motors.left(65)
    t = time.time()
    while True:
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
            maplogger.log(heading=compass.getHeading())
        else:
            maplogger.log(heading=compass.getHeading(), walls=data)

        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    motors.stop()
    robot.clean()
    #f.close()
    maplogger.close()