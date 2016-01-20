import robot
from robot import motors
from robot import compass

compass.calibrate(10)
input("JAJA")

motors.forward()

try:
    while True:
        pass
except:
    motors.stop()
    robot.clean()