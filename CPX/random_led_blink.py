from adafruit_circuitplayground.express import cpx
from time import sleep
from random import random

while True:
    delay = random()
    cpx.red_led = True
    sleep(delay)
    cpx.red_led = False
    sleep(delay)
    print(delay)