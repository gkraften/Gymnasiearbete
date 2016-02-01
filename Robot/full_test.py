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
    threading.Thread(target=supermagiskt).start()

    distance.start_measuring(count)
    motors.forward(math.pi/2)
    time.sleep(5)

    distance.stop_measuring()
    motors.stop()
    robot.turn_to(math.pi, math.radians(4))
    distance.start_measuring(count)
    motors.forward(math.pi)
    time.sleep(3)
except KeyboardInterrupt:
    pass
finally:
    done = True
    distance.stop_measuring()
    maplogger.close()
    motors.stop()
    robot.clean()