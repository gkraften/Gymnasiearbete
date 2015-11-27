import robot.compass as compass
import robot.motors as motors
import time

try:
    motors.left(50)
    with open("data.csv", "w") as f:
        while True:
            data = compass.readAxis()
            print("{},{}".format(data[0], data[1]), file=f)
            time.sleep(1/220)
except:
    motors.stop()
    compass.sleep()