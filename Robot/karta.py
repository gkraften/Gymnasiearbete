from robot import compass
from robot import motors
from robot import ultrasonic
import robot
import vector
import time
import math
from subprocess import call
import maplogger

call(["service", "apache2", "start"])

#f = open("/var/www/map.txt", "w")
maplogger.initialize("/var/www/map.txt")

try:
    compass.calibrate(5)
    input("Tryck på enter för att starta ")
    motors.left(60)
    t = time.time()
    while time.time() - t < 10:
        u = vector.from_polar(ultrasonic.get_middle(), compass.getHeading())
        #print("{},{}".format(u.x, u.y), file=f)

        v = vector.from_polar(ultrasonic.get_left(), compass.angleDifference(compass.getHeading(), -math.radians(30)))
        #print("{},{}".format(v.x, v.y), file=f)

        w = vector.from_polar(ultrasonic.get_right(), compass.angleDifference(compass.getHeading(), math.radians(30)))
        #print("{},{}".format(w.x, w.y), file=f)

        maplogger.log(walls=[[u.x, u.y], [v.x, v.y], [w.x, w.y]])

        time.sleep(0.05)
finally:
    motors.stop()
    robot.clean()
    #f.close()
    maplogger.close()