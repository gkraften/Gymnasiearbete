import RPi.GPIO as GPIO
import robot.pins as pins
import robot

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

def stop():
    LEFT.stop()
    RIGHT.stop()

def forward():
    LEFT.forward(80)
    RIGHT.forward(100)

def backward():
    LEFT.backward(100)
    RIGHT.backward(100)

def left(speed=100):
    LEFT.backward(speed)
    RIGHT.forward(speed)

def right(speed=100):
    LEFT.forward(speed)
    RIGHT.backward(speed)