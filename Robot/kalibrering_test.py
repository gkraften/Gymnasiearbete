import robot.motors
import sys

#Osäkert om det här programmet gör det jag vill

if len(sys.argv) != 3:
    print("Du måste skriva kalibreringsskit")
    sys.exit()

left = int(sys.argv[1])
right = int(sys.argv[2])

if left > right:
    robot.motors.LEFT.forward(100)
    robot.motors.RIGHT.forward(100*right/left)
elif right > left:
    robot.motors.RIGHT.forward(100)
    robot.motors.LEFT.forward(100*left/right)
elif right == left:
    robot.motors.forward(100)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    robot.clean()