from microbit import *
from random import randint
import radio

radio.on()
radio.config(channel=7)

while True:
    message = radio.receive()
    if message is not None:
        display.show(message)
        sleep(5000)
        display.clear()
