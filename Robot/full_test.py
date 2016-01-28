from robot import compass
from robot import motors
from robot import distance
import robot
import math
import vector

n = vector.Vector(0, 0)

def count():
    global n
    n += vector.from_polar(distance.HALF_CIRCUMFERENCE, compass.getHeading())

def avsluta():
    print("Batteriet är slut!")
    robot.clean()
    robot.halt()

try:
    robot.on_battery_low(avsluta)
    compass.calibrate(5)
    robot.turn_to(math.pi/2, math.radians(4))
    input("Enter")
    distance.start_measuring(count)
    motors.forward(math.pi/2)
    input("Tryck på enter")
    motors.stop()
    distance.stop_measuring()
    print("Avstånd: {}".format(n.length()))
finally:
    motors.stop()
    robot.clean()