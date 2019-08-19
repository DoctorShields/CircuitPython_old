#pylint: disable-msg=import-error

import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# Built in neopixel
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=1)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

######################### MAIN LOOP ##############################
red = (255,0,0)
grn = (0,255,0)
blu = (0,0,255)
colors = [red, grn, blu]
print("running")
while True:
    for c in colors:
        dot[0] = tuple(c)
        time.sleep(.1)
        led.value = not led.value