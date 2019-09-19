import time
import board    #pylint: disable-msg=import-error
from rgb import RGB

r = board.D2
g = board.D3
b = board.D4

myRGB = RGB(r,g,b)

print("go")

while True:
    myRGB.red()
    time.sleep(0.1)
    myRGB.green()
    time.sleep(0.1)
    myRGB.blue()
    time.sleep(0.1)
    myRGB.cyan()
    time.sleep(0.1)
    myRGB.magenta()
    time.sleep(0.1)
    myRGB.yellow()
    time.sleep(0.1)
    myRGB.white()
    time.sleep(0.1)
    myRGB.black()
    time.sleep(0.1)
    myRGB.rainbow()