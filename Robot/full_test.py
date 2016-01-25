from robot import compass
from robot import motors
from robot import distance
import robot
import math

n = 0

def count():
    global n
    n += 1

try:
    compass.calibrate(5)
    robot.turn_to(math.pi/2)
    input("Enter")
    distance.start_measuring(count)
    motors.forward(math.pi/2)
    input("Tryck på enter")
    motors.stop()
    distance.stop_measuring()
    print("Antal halva varv: {}".format(d))
    robot.turn_to(3*math.pi/2)
    robot.forward(3*math.pi/2)
    input("Tryck på enter för att stanna")
finally:
    motors.stop()
    robot.clean()