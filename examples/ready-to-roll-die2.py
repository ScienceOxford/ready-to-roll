from microbit import *
import audio
from random import randint
import radio

radio.on()
radio.config(channel=7)

while True:
    message = radio.receive()
    if message is not None:
        display.show(message)
        audio.play(Sound.GIGGLE)
        sleep(5000)
        display.clear()
