import time
import digitalio  #pylint: disable-msg=import-error
import analogio   #pylint: disable-msg=import-error
import board      #pylint: disable-msg=import-error
import pulseio    #pylint: disable-msg=import-error

# make a digital input pin for the photo interrupter
photo = digitalio.DigitalInOut(board.D2)
photo.direction = digitalio.Direction.INPUT
photo.pull = digitalio.Pull.UP
# make an analog input pin for the potentiometer
pot = analogio.AnalogIn(board.A1)
# make an analog output pin for the motor transistor (or a PWM?)
#motor = analogio.AnalogOut(board.A0)
motor2 = pulseio.PWMOut(board.D8, frequency=5000, duty_cycle=0)

# some initial values
photoState = True
lastPhoto = True
potVal = 0
lastTime = 0
count = 0

print("starting")

while True:
    photoState = photo.value
    now = time.monotonic()
    # did the photointerrupter get tripped?
    if photoState and not lastPhoto:
        count += 1
    lastPhoto = photoState
    # get the pot val and set the motor speed (both go zero to 65535, so that works out)
    potVal = pot.value
    #motor.value = potVal
    motor2.duty_cycle = potVal
    # has it been a second?
    if now > lastTime + 1:
        RPM = count*60/5
        print(RPM)
        count = 0
        lastTime = now
