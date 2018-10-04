from microbit import *
import neopixel
import random
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()

np = neopixel.NeoPixel(pin0, 7)

# dictionary to associate a string number with the neopixels needed for pattern
numbers = {"1": [0, 0, 0, 1, 0, 0, 0], "2": [0, 1, 0, 0, 0, 1, 0],
           "3": [1, 0, 0, 1, 0, 0, 1], "4": [1, 0, 1, 0, 1, 0, 1],
           "5": [1, 0, 1, 1, 1, 0, 1], "6": [1, 1, 1, 0, 1, 1, 1]}

# dictionary to associate a string colour with the RGB values for that colour
colours = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255),
           "orange": (255, 165, 0), "bluepurple": (165, 0, 255),
           "redpurple": (255, 0, 165), "pink": (255, 165, 165),
           "yellow": (255, 255, 0), "bluegreen": (0, 165, 255),
           "greenblue": (0, 255, 165), "white": (255, 255, 255),
           "yellowgreen": (165, 255, 0)}

# function to iterate through the neopixels and, based on chosen number,
# turn each off or on to chosen colour
def show_number(time):
    for index, pixel in enumerate(number):
        if pixel == 0:
            np[index] = (0, 0, 0)
        else:
            np[index] = colour
    np.show()
    sleep(time)

while True:
    message = radio.receive()
    # message must be in format 'number colour' e.g. '3 red' or 'two green'
    while message is None:
        # if no messages, cycle through random numbers & colours
        number = random.choice(list(numbers.values()))
        colour = random.choice(list(colours.values()))
        show_number(500)
        message = radio.receive()
    try:
        # split message into ["number", "colour"] e.g. ["3", "red"] & show
        roll = message.split()
        number = numbers[roll[0]]
        colour = colours[roll[1]]
        show_number(2000)
    except (KeyError):
        # if message not in correct format, so item not in dict, then move on
        pass
