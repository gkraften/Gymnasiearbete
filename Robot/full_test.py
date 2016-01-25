from robot import compass
from robot import motors
import robot
import math

try:
    compass.calibrate(5)
    robot.turn_to(math.pi / 2)
    motors.forward()
    input("Du är fett ful")
    motors.stop()
    robot.turn_to(3*math.pi/2)
    motors.forward()
except KeyboardInterrupt:
    pass
finally:
    robot.clean()