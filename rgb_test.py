import time
import board    #pylint: disable-msg=import-error
import pulseio  #pylint: disable-msg=import-error
 
r = pulseio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
g = pulseio.PWMOut(board.D3, frequency=5000, duty_cycle=0)
b = pulseio.PWMOut(board.D4, frequency=5000, duty_cycle=0)
 
while True:
    led.duty_cycle = 2 ** 15
    time.sleep(0.05)