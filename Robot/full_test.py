from robot import compass
from robot import motors
import robot
import math

try:
    print("Kalibrerar")
    compass.calibrate(5)
    print("Snurrar mot väst")
    robot.turn_to(math.pi / 2)
    print("Åker frammåt")
    motors.forward()
    input("Du är fett ful")
    motors.stop()
    print("Snurrar mot öst")
    robot.turn_to(3*math.pi/2)
    print("Åker framåt")
    motors.forward()
except KeyboardInterrupt:
    pass
finally:
    robot.clean()