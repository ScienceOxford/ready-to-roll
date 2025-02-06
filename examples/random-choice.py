# Imports go at the top
from microbit import *
from random import randint, choice
import music

one = '00000:00000:00900:00000:00000'
two = '90000:00000:00000:00000:00009'
three = '90000:00000:00900:00000:00009'
four = '90009:00000:00000:00000:90009'
five = '90009:00000:00900:00000:90009'
six = '90009:00000:90009:0000:90009'

numbers = [one, two, three, four, five, six]

# Code in a 'while True:' loop repeats forever
while True:
    if accelerometer.was_gesture('shake'):
        roll = choice(numbers)
        display.show(Image(roll))
        sleep(1000)
