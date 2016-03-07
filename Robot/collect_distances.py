from robot import ultrasonic
import robot
from time import sleep

n = int(input("Hur många punkter från varje sensor?"))

with open("distances.csv", "w") as f:
    for i in range(n):
        d1 = ultrasonic._LEFT.distance()
        d2 = ultrasonic._MIDDLE.distance()
        d3 = ultrasonic._RIGHT.distance()
        print("{},{},{}".format(d1, d2, d3), file=f)
        sleep(0.05)
        if i % int(0.01*n) == 0:
            print("{}%".forma(100*i/n))

robot.clean()