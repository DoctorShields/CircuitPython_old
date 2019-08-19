#pylint: disable-msg=import-error
import board
import digitalio
import time

#led = digitalio.DigitalInOut(board.D1)
led = digitalio.DigitalInOut(board.D13)

# digital IO pins are inputs by default
led.direction = digitalio.Direction.OUTPUT

print("blink")
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)