import robot
from robot import motors
from robot import compass

compass.calibrate(10)

input("Tryck på enter för att starta")

try:
    motors.forward()
    while True:
        pass
except:
    motors.stop()
    robot.clean()