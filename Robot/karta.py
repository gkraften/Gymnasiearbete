from robot import compass
from robot import motors
from robot import range
import robot
import vector
import time

f = open("map.txt", "w")

try:
    compass.calibrate(5)
    motors.left(70)
    while True:
        v = vector.from_polar(range.MIDDLE.distance(), compass.getHeading())
        print("{},{}".format(v.x, v.y), file=f)
        time.sleep(0.1)
finally:
    motors.stop()
    robot.clean()
    f.close()