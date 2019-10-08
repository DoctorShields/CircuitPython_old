from digitalio import DigitalInOut, Direction  #pylint: disable=import-error
import board                                   #pylint: disable=import-error
import time

pin = 8
led = DigitalInOut(getattr(board,"D"+str(pin)))
led = DigitalInOut(board.D8)
led.direction = Direction.OUTPUT

print("blinky")

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)