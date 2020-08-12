import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

BUZ = 38
BUTTON = 12
led_pin = 11

BUTTON_PRESSED = 0
ON = 1
OFF = 0

GPIO.setup(BUZ, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(BUZ, 1)

light_on = False

while 1:
    if (GPIO.input(BUTTON) == 1):
        GPIO.output(BUZ, 0)
        GPIO.output(led_pin, 1)

        print("ON!")

    if (GPIO.input(BUTTON) == 0):
        GPIO.output(BUZ, 1)
        GPIO.output(led_pin, 0)

        print("OFF!")

    time.sleep(1)
