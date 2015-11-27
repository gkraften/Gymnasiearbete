import robot.compass as compass
import robot.motors as motors
import RPi.GPIO as GPIO
import time
import sys

compass.wake()
compass.setHighSpeedDataRate()

x_list = []
y_list = []

try:
    if len(sys.argv) == 2 and sys.argv[1] == "-a":
        motors.right(50)

    while True:
        x, y, z = compass.readAxisData()

        x_list.appen(x)
        y_list.append(y)
        if (len(x_list) >= 2 and len(y_list) >= 2):
            print("{} {} {} {}".format(min(x_list), max(x_list), min(y_list), max(y_list)))

        time.sleep(1/220)
except KeyboardInterrupt:
    print("x offset: {}\ty offset: {}".format((min(x_list) + max(x_list))/2, (min(y_list) + max(y_list))/2))
finally:
    compass.setNormalSpeedDataRate()
    compass.sleep()
    GPIO.cleanup()