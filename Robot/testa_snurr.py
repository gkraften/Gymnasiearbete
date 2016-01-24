import robot
from robot import motors
from robot import compass
import math

compass.calibrate(10)

cmd = input("skriv gradtal (q för att avsluta) ")
try:
    while cmd != "q":
        nums = cmd.split(" ")
        robot.turn_to(math.radians(float(nums[0])))
        print("Fel: {}°".format(math.degrees(compass.angleDifference(fmath.radians(float(nums[0]), compass.getHeading()))))
        cmd = input("skriv gradtal (q för att avsluta) ")
except KeyboardInterrupt:
    pass
finally:
    motors.stop()
    robot.clean()