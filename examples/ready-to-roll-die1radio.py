from microbit import *
from random import randint
import radio

radio.on()
radio.config(channel=12)

while True:
    if accelerometer.was_gesture("shake"):
        roll = randint(1, 6)
        display.show(roll)
        radio.send(str(roll))
        sleep(5000)
        display.clear()
