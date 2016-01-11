import robot
from robot import motors
from robot import compass
import time
from controller import PID
import sys

if len(sys.argv) == 1:
    print("Du måste välja kp")
    sys.exit()

pid = PID(float(sys.argv[1]), 0, 0, -50, 50)
pid.set_target(0)

compass.wake()
motors.LEFT.forward(100)
motors.RIGHT.forward(100)

try:
    l_speed = 100
    r_speed = 100
    last = time.time()
    last_direction = compass.getHeading()
    while True:
        dt = time.time() - last
        last = time.time()

        direction = compass.getHeading()
        ret = pid.update(last_direction - direction, dt)
        last_direction = direction

        if ret > 0:
            r_speed = 100
            l_speed = 100 - ret
        if ret < 0:
            r_speed = 100 + ret
            l_speed = 100

        motors.LEFT.forward(l_speed)
        motors.RIGHT.forward(r_speed)

        time.sleep(0.05)
except:
    print("Vänster: {}%\tHöger: {}%".format(l_speed, r_speed))
    robot.clean()
    compass.sleep()