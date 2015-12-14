import robot.compass as compass
import robot.motors as motors
import time

try:
    motors.left(100)
    with open("data.csv", "w") as f:
        while True:
            data = compass.readAxisData()
            print("{},{}".format(data[0], data[1]), file=f)
            time.sleep(1/220)
except:
    motors.stop()
    compass.sleep()