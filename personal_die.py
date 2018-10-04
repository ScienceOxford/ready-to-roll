from microbit import *
from random import randint, choice
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()

one = Image('00000:'
            '00000:'
            '00900:'
            '00000:'
            '00000:')

two = Image('00000:'
            '00000:'
            '09090:'
            '00000:'
            '00000:')

three = Image('00000:'
              '00090:'
              '00900:'
              '09000:'
              '00000:')

four = Image('00000:'
             '09090:'
             '00000:'
             '09090:'
             '00000:')

five = Image('00000:'
             '09090:'
             '00900:'
             '09090:'
             '00000:')

six = Image('00000:'
            '09090:'
            '09090:'
            '09090:'
            '00000:')

numbers = [one, two, three, four, five, six]

while True:
    if accelerometer.was_gesture("shake"):
            digit = randint(1,6)
            display.show(digit)
            radio.send(str(digit) + " red")
            sleep(500)
    if button_a.was_pressed():
            number = choice(numbers)
            display.show(number)
            sleep(500)
