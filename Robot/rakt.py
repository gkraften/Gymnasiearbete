import robot
from robot import motors
from robot import compass
import time
from controller import PID
import sys
import math

def battery_low():
    print("Lågt batteri!")
    robot.clean()
    robot.halt()

robot.on_battery_low(battery_low)

pid = PID(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), -50, 50)
pid.set_target(math.pi/2)
pid.difference = compass.angleDifference

compass.calibrate(10)

input("Tryck på enter")

motors.LEFT.forward(100)
motors.RIGHT.forward(100)

l_speed = 100
r_speed = 100
last = time.time()
while True:
    try:
        dt = time.time() - last
        last = time.time()

        direction = compass.getHeading()
        ret = pid.update(direction, dt)

        if ret < 0:
            r_speed = 100 + ret
            l_speed = 100
        if ret > 0:
            r_speed = 100
            l_speed = 100 - ret

        motors.LEFT.forward(l_speed)
        motors.RIGHT.forward(r_speed)

        time.sleep(0.25)
    except KeyboardInterrupt:
        motors.stop()
        cmd = input("Skriv q för att avsluta, tryck endast på enter för att fortsätta")
        if cmd == "q":
            print("Vänster: {}%\tHöger: {}%".format(l_speed, r_speed))
            break
    except:
        motors.stop()
        break
robot.clean()