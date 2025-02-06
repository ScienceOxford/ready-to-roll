# Imports go at the top
from microbit import *
from random import randint, choice
import music


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')
