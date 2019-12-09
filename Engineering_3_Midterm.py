# import my modules
import time
import board
import pulseio
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
from adafruit_motor import servo

# initialize stuff, including pins
count = 0
vals = [0,0,0,0]
pins = [board.D5, board.D4, board.D3, board.D2]
photoPins = [board.D9, board.D10]
oldPhotos = [False, False]
pwm = pulseio.PWMOut(board.D8, duty_cycle=2**15,frequency=50)
myServo = servo.Servo(pwm)
pot = AnalogIn(board.A1)

# make photoInterrupter array
photos = []
for pin in photoPins:
    photos.append(DigitalInOut(pin))
for photo in photos:
    photo.direction = Direction.INPUT
    photo.pull = Pull.UP

# make LED array
leds = []
for pin in pins:
    leds.append(DigitalInOut(pin))
for led in leds:
    led.direction = Direction.OUTPUT

# map pot val to 0-180
def potVal(pin):
    return pin.value * 180 / 65536

while True:
    # set the servo speed
    myServo.angle = potVal(pot)
    # use a bitwise AND to figure out LED values
    for i, led in enumerate(leds):
       s =int(2**i & count)
       leds[3-i].value = 1 if s != 0 else 0
    # did either photo interrupter get tripped?
    for i, photo in enumerate(photos):
        if(photo.value and not oldPhotos[i]):
            count += 1
    if count == 16:
        count = 0
    for i, photo in enumerate(oldPhotos):
        oldPhotos[i] = photos[i].value
    time.sleep(.01)