from robot import compass
from robot import motors
from robot import distance
from robot import ultrasonic
import robot
import math
import vector
import time
import threading

n = vector.Vector(0, 0)
done = False
f = open("/var/www/karta.txt", "w")

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

        l = ultrasonic.get_left()

        r = ultrasonic.get_right()

        s = "{},{} {}".format(n.x, n.y, compass.getHeading())
        data = []
        if m <= 300 and m >= 15:
            data.append([u.x, u.y])
            s += " 2:{}".format(m)
        if l <= 300 and l >= 15:
            data.append([v.x, v.y])
            s += " 1:{}".format(l)
        if r <= 300 and l >= 15:
            data.append([w.x, w.y])
            s += " 3:{}".format(r)

        if len(data) != 0:
            for d in data:
                s += " {}".format(d)
            print(s, )
        time.sleep(0.2)

try:
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
            time.sleep(0.1)
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()
        elif right <= 50:
            distance.stop_measuring()
            motors.stop()
            motors.left()
            time.sleep(0.5)
            motors.stop()
            time.sleep(0.1)
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()
        elif middle <= 50:
            distance.stop_measuring()
            motors.stop()
            motors.right()
            time.sleep(0.5)
            motors.stop()
            time.sleep(0.1)
            last = compass.getHeading()
            distance.start_measuring(count)
            motors.forward()

        if time.time() - t >= 0.5:
            if abs(compass.angleDifference(compass.getHeading(), last)) >= math.radians(15):
                distance.stop_measuring()
                motors.stop()
                done = True
                logger.join()
                a = compass.getHeading()
                compass.calibrate(3)
                done = False
                logger = threading.Thread(target=supermagiskt)
                logger.start()
                robot.turn_to(a, math.radians(20))
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
    f.close()
    robot.clean()