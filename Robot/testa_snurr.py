import robot
from robot import motors
from robot import compass
import math

compass.calibrate(10)

cmd = input("skriv gradtal, kp, ki, kd (q för att avsluta) ")
try:
    while cmd != "q":
        nums = cmd.split(" ")
        robot.turn_to(math.radians(float(nums[0])), float(nums[1]), float(nums[2]), float(nums[3]))
        cmd = input("skriv gradtal, kp, ki, kd (q för att avsluta) ")
except KeyboardInterrupt:
    pass
finally:
    motors.stop()
    robot.clean()