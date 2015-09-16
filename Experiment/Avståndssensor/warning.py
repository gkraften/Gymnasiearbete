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

    return int(round((stop - start) * 17150, 0))


trig = 23
echo = 24
led = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(trig, GPIO.OUT, initial=False)
GPIO.setup(led, GPIO.OUT, initial=False)
GPIO.setup(echo, GPIO.IN)

time.sleep(0.1)

try:
    while True:
        d = distance()
        if d < 20:
            GPIO.output(led, True)
        elif d >= 20:
            GPIO.output(led, False)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
