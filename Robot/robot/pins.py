import RPi.GPIO as GPIO

BATTERY = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(BATTERY, GPIO.IN, pull_up_down=GPIO.PUD_UP)