from robot import compass
from robot import motors
import robot
import math

try:
    compass.calibrate(5)
    while True:
        robot.turn_to(math.pi / 2, math.radians(4))
        motors.forward()
        input("Du är fett ful")
        motors.stop()
        robot.turn_to(3*math.pi/2, math.radians(4))
        motors.forward()
        input("VÄND FÖR I HELVETE!!!")
        motors.stop()
finally:
    motors.stop()
    robot.clean()