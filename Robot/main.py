import robot.motors
import time
import RPi.GPIO as GPIO

#Ignorera den här funktionen. Jag vet knappt själv hur den funkar
#/G
def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

get = getch()

try:
    while True:
        cmd = get()
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