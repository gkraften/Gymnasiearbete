import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2

        GPIO.setup(pin1, GPIO.OUT, initial=False)
        GPIO.setup(pin2, GPIO.OUT, initial=False)

    def forward(self):
        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)

    def backward(self):
        GPIO.output(self.pin2, True)
        GPIO.output(self.pin1, False)

    def stop(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)

LEFT = Motor(13, 11)
RIGHT = Motor(16, 18)

def stop():
    LEFT.stop()
    RIGHT.stop()