import board
import time
import analogio
import digitalio

led1 = analogio.AnalogOut(board.A0)
led2 = digitalio.DigitalInOut(board.D2)
led2.direction = digitalio.Direction.OUTPUT

print("blink")

while True:
    for i in range(0,255):
        led2.value = i
        time.sleep(.1)