import robot.motors
import robot.distance
import robot.pins as pins
import robot
import random
import time
import RPi.GPIO as GPIO

robot.on_battery_low(lambda: print("Lågt batteri!"))
print(GPIO.input(pins.BATTERY))

robot.motors.forward()

try:
    while True:
        if (robot.distance.get_mid() < 30 and robot.distance.get_left() < 30 and robot.distance.get_right() < 30):
            robot.motors.backward()
            time.sleep(1)
            random.choice([robot.motors.left, robot.motors.right])()
            time.sleep(0.5)
            robot.motors.forward()
        elif (robot.distance.get_mid() < 20):
            random.choice([robot.motors.left, robot.motors.right])()
            time.sleep(0.5)
            robot.motors.forward()
        elif (robot.distance.get_left() < 20):
            robot.motors.right()
            time.sleep(0.5)
            robot.motors.forward()
        elif (robot.distance.get_right() < 20):
            robot.motors.left()
            time.sleep(0.5)
            robot.motors.forward()
        time.sleep(0.1)
finally:
    GPIO.cleanup()