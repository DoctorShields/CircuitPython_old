import board
import time
import pulseio

led = pulseio.PWMOut(board.D3, duty_cycle=0, frequency=5000)

print("fade")

while True:
    for i in range(1,100):
        led.duty_cycle = int(i * 2**16 / 100)
        time.sleep(.01)
    for i in range(1,100):
        led.duty_cycle = 2**16 - int(i * 2**16 / 100)
        time.sleep(.01)
