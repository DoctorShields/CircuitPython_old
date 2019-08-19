import board
import time
import neopixel

# Built in neopixel
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

red = (255,0,0)
grn = (0,255,0)
blu = (0,0,255)
colors = [red, grn, blu]
print("running")

while True:
    for c in colors:
        dot.fill(tuple(c))
        time.sleep(.5)