import robot
from robot import motors
from robot import compass
import time
from controller import PID
import sys

pid = PID(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), -50, 50)
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
        ret = pid.update(direction - last_direction, dt)
        print(ret)
        last_direction = direction

        if ret > 0:
            r_speed = 100
            l_speed = 100 - ret
        if ret < 0:
            r_speed = 100 + ret
            l_speed = 100

        motors.LEFT.forward(l_speed)
        motors.RIGHT.forward(r_speed)

        time.sleep(0.5)
except:
    print("Vänster: {}%\tHöger: {}%".format(l_speed, r_speed))
    robot.clean()
    compass.sleep()