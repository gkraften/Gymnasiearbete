import robot.compass as compass

compass.wake()
compass.setHighSpeedDataRate()

x_max = None
x_min = None
y_max = None
y_min = None

try:
    while True:
        x, y, z = compass.readAxisData()
        if x_max is None or x > x_max:
            x_max = x
        elif x_min is None or x < x_min:
            x_min = x

        if y_max is None or y > y_max:
            y_max = y
        elif y_min is None or y < y_min:
            y_min = y
except KeyboardInterrupt:
    x_offset = -abs(x_max - x_min)/2
    x_scale = 1/abs(x_max - x_min)
    y_offset = -abs(y_max - y_min)/2
    y_scale = 1/abs(y_max - y_min)

    print("x_offset = {}".format(x_offset))
    print("x_sxale = {}".format(x_scale))
    print("y_offset = {}".format(y_offset))
    print("y_scale = {}".format(y_scale))
finally:
    compass.setNormalSpeedDataRate()
    compass.sleep()