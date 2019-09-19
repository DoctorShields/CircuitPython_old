import time
import board      #pylint: disable-msg=import-error
import pulseio    #pylint: disable-msg=import-error

# Metro M0 Express has PWM on the following pins: A2, A3, A4, D0, RX, D1, TX,
# D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, SDA, SCL, 
# NEOPIXEL, SCK, MOSI, MISO.

r1 = pulseio.PWMOut(board.D1, frequency=5000, duty_cycle=0)
g1 = pulseio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
b1 = pulseio.PWMOut(board.D3, frequency=5000, duty_cycle=0)
r2 = pulseio.PWMOut(board.D4, frequency=5000, duty_cycle=0)
g2 = pulseio.PWMOut(board.D5, frequency=5000, duty_cycle=0)
b2 = pulseio.PWMOut(board.D7, frequency=5000, duty_cycle=0)

maxVal = 2**16-1

print("starting")

def red():
    print("red")
    r1.duty_cycle = 0
    g1.duty_cycle = maxVal
    b1.duty_cycle = maxVal
    r2.duty_cycle = 0
    g2.duty_cycle = maxVal
    b2.duty_cycle = maxVal

def green():
    print("green")
    r1.duty_cycle = maxVal
    g1.duty_cycle = 0
    b1.duty_cycle = maxVal
    r2.duty_cycle = maxVal
    g2.duty_cycle = 0
    b2.duty_cycle = maxVal

def blue():
    print("blue")
    r1.duty_cycle = maxVal
    g1.duty_cycle = maxVal
    b1.duty_cycle = 0
    r2.duty_cycle = maxVal
    g2.duty_cycle = maxVal
    b2.duty_cycle = 0

def rainbow():
    g1.duty_cycle = 0
    g2.duty_cycle = 0
    b1.duty_cycle = maxVal
    b2.duty_cycle = maxVal
    for i in range(0,2**16-1,64):
        r1.duty_cycle = i
        r2.duty_cycle = i
        time.sleep(0.005)
    for i in range(0,2**16-1,64):
        b1.duty_cycle = 2**16-1-i
        b2.duty_cycle = 2**16-1-i
        time.sleep(0.005)

while True:
    red()
    time.sleep(1)
    green()
    time.sleep(1)
    blue()
    time.sleep(1)
    rainbow()