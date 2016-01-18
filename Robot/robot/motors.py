import RPi.GPIO as GPIO
import robot.pins as pins
import robot
from timer import  Timer
from controller import PID
import time
import robot.compass as compass

class Motor:
    def __init__(self, pin1, pin2):
        GPIO.setup(pin1, GPIO.OUT, initial=False)
        GPIO.setup(pin2, GPIO.OUT, initial=False)

        self.pin1 = GPIO.PWM(pin1, 200)
        self.pin2 = GPIO.PWM(pin2, 200)

        self.pin1.start(0)
        self.pin2.start(0)

        self.spinning = False

    def forward(self, speed=100):
        if not self.spinning:
            robot.pause_battery_detection()
            self.spinning = True
        self.pin1.ChangeDutyCycle(speed)
        self.pin2.ChangeDutyCycle(0)

    def backward(self, speed=100):
        if not self.spinning:
            robot.pause_battery_detection()
            self.spinning = True
        self.pin2.ChangeDutyCycle(speed)
        self.pin1.ChangeDutyCycle(0)

    def stop(self):
        self.pin1.ChangeDutyCycle(0)
        self.pin2.ChangeDutyCycle(0)
        if self.spinning:
            robot.resume_battery_detection()
            self.spinning = False

LEFT = Motor(pins.MOTOR_LEFT_1, pins.MOTOR_LEFT_2)
RIGHT = Motor(pins.MOTOR_RIGHT_1, pins.MOTOR_RIGHT_2)

class _MotorController(Timer):
    def __init__(self):
        super().__init__(0.25)

        self.pid = PID(25, 20, 30, -50, 50)
        self.pid.set_target(0)
        self.drive_forward = False
        self.drive_backward = False
        self.t = 0
        self.last = 0
        self.r_speed = 100
        self.l_speed = 100

    def forward(self):
        self.backward = False
        self.forward = True

    def backward(self):
        self.backward = True
        self.forward = False

    def run(self):
        dt = time.time() - self.t
        t_cpy = self.t
        self.t = time.time()

        if t_cpy != 0:
            now = compass.getHeading()
            ret = self.pid.update(compass.angleDifference(now, self.last))
            self.last = now

            if ret < 0:
                self.r_speed = 100
                self.l_speed = 100 + ret
            if ret > 0:
                self.r_speed = 100 - ret
                self.l_speed = 100

        if self.drive_forward:
            LEFT.forward(self.l_speed)
            RIGHT.forward(self.r_speed)
        elif self.drive_backward:
            LEFT.backward(self.l_speed)
            RIGHT.backward(self.r_speed)

_CONTROLLER = _MotorController()

def stop():
    _CONTROLLER.pause()
    LEFT.stop()
    RIGHT.stop()

def forward():
    _CONTROLLER.forward()
    _CONTROLLER.start()

def backward():
    _CONTROLLER.backward()
    _CONTROLLER.start()

def left(speed=100):
    LEFT.backward(speed)
    RIGHT.forward(speed)

def right(speed=100):
    LEFT.forward(speed)
    RIGHT.backward(speed)