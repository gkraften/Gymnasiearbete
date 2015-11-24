import robot.compass as compass
import time

compass.wake()
compass.setHighSpeedDataRate()

x_max = None
x_min = None
y_max = None
y_min = None

try:
    x, y, z = compass.readAxisData()
    x_max = x
    x_min = x
    y_max = y
    y_min = y
    while True:
        x, y, z = compass.readAxisData()
        x_max = max(x, x_max)
        x_min = min(x, x_min)
        y_max = max(y, y_max)
        y_min = min(y, y_min)

        print("{} {} {} {}".format(x_min, x_max, y_min, y_max))

        time.sleep(1/220)
except KeyboardInterrupt:
    print("x offset: {}\ty offset: {}".format((x_min + x_max)/2, (y_min + y_max)/2))
finally:
    compass.setNormalSpeedDataRate()
    compass.sleep()