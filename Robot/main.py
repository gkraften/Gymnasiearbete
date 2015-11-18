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
        elif cmd == "q":
            robot.motors.stop()
            break
        elif cmd == "l":
            robot.motors.LEFT.backward()
            robot.motors.RIGHT.forward()
        elif cmd == "r":
            robot.motors.LEFT.forward()
            robot.motors.RIGHT.backward()
finally:
    GPIO.cleanup()