import RPi.GPIO as GPIO
import time


def distance():
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)

    while GPIO.input(echo) == 0:
        pass
    start = time.time()

    while GPIO.input(echo) == 1:
        pass

    stop = time.time()

    return (stop - start) * 17150


trig = 23
echo = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(trig, GPIO.OUT)
GPIO.output(trig, 0)

GPIO.setup(echo, GPIO.IN)

time.sleep(0.1)

try:
    while True:
        print(int(round(distance(), 0)))
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
