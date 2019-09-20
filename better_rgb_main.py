import time
import board    #pylint: disable-msg=import-error
from rgb import RGB

pins1 = [board.D1, board.D2, board.D3]
pins2 = [board.D4, board.D5, board.D7]
delay = 1

myRGB1 = RGB(pins1)
myRGB2 = RGB(pins2)

print("go")

while True:
    myRGB1.red()
    myRGB2.green()
    time.sleep(delay)
    myRGB1.green()
    myRGB2.red()
    time.sleep(delay)
    myRGB1.blue()
    myRGB2.cyan()
    time.sleep(delay)
    myRGB1.cyan()
    myRGB2.blue()
    time.sleep(delay)
    myRGB1.magenta()
    myRGB2.yellow()
    time.sleep(delay)
    myRGB1.yellow()
    myRGB2.magenta()
    time.sleep(delay)
    myRGB1.white()
    myRGB2.white()
    time.sleep(delay)
    myRGB1.black()
    myRGB2.black()
    time.sleep(delay)
    myRGB1.rainbow()
    myRGB2.rainbow()