import robot
from robot import motors
from robot import compass
import math
import maplogger
from threading import Thread
import time

compass.calibrate(10)

maplogger.initialize()

cmd = input("skriv gradtal (q för att avsluta) ")
try:
    while cmd != "q":
        nums = cmd.split(" ")
        turner = Thread(target=robot.turn_to, args=(math.radians(float(nums[0])), math.radians(4)))
        turner.start()

        while turner.isAlive():
            maplogger.log(heading=compass.getHeading())
            time.sleep(0.1)

        print("Fel: {}°".format(math.degrees(compass.angleDifference(math.radians(float(nums[0])), compass.getHeading()))))
        cmd = input("skriv gradtal (q för att avsluta) ")
except KeyboardInterrupt:
    pass
finally:
    motors.stop()
    robot.clean()
    maplogger.close()