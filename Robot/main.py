import robot.motors
import time
import RPi.GPIO as GPIO

try:
    while True:
        cmd = input("> ")
        if cmd == "f":
            robot.motors.LEFT.forward()
            robot.motors.RIGHT.forward()
        elif cmd == "b":
            robot.motors.LEFT.backward()
            robot.motors.RIGHT.backward()
        elif cmd == "s":
            robot.motors.stop()
finally:
    GPIO.cleanup()