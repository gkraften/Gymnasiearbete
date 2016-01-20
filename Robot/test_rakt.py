import robot
from robot import motors
from robot import compass

def battery_low():
    print("Lågt batteri! Stänger av...")
    robot.clean()
    robot.halt()

robot.on_battery_low(battery_low)

compass.calibrate(10)

input("Tryck på enter för att starta")

try:
    motors.forward()
    while True:
        pass
except:
    motors.stop()
    robot.clean()