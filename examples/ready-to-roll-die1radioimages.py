from microbit import *
from random import randint, choice
import radio

radio.on()
radio.config(channel=12)

one = "00000:00000:00900:00000:00000"
two = "00000:09000:00000:00090:00000"
three = "90000:00000:00900:00000:00009"
four = "00000:09090:00000:09090:00000"
five = "90009:00000:00900:00000:90009"
six = "09090:00000:09090:00000:09090"

numbers = [one, two, three, four, five, six]

while True:
    if accelerometer.was_gesture("shake"):
        roll = choice(numbers)
        display.show(Image(roll))
        radio.send(str(roll))
        sleep(5000)
        display.clear()
