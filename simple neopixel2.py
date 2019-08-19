import board
import time
import neopixel

# Built in neopixel
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

red = (255,0,0)
grn = (0,255,0)
blu = (0,0,255)
yel = (255,255,0)
mag = (255,0,255)
cya = (0,255,255)
whi = (255,255,255)

colors = [red, grn, blu, yel, mag, cya, whi]
print("running")

while True:
    for c in colors:
        dot.fill(tuple(c))
        time.sleep(.5)