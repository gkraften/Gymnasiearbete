import robot
import robot.motors
import robot.compass
import robot.distance
import vector

p = vector.Vector(0, 0)

def battery_low():
    print("Lågt batteri! Stänger av...")
    robot.clean()
    robot.halt()

def moved():
    global p
    p += vector.from_polar(robot.distance.HALF_CIRCUMFERENCE, robot.compass.getHeading())

robot.on_battery_low(battery_low)

robot.compass.calibrate(10)
input("Tryck på enter för att starta. Tryck på ctrl+C för att stoppa.")

robot.distance.start_measuring(moved)
robot.motors.forward()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    robot.motors.stop()
    print("Avståndet till origo är {}cm".format(p.length()))
    robot.clean()