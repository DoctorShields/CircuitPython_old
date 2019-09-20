from pulseio import PWMOut #pylint: disable-msg=import-error
from time import sleep

class RGB:

    full = 2**16-1

    def __init__(self, pins):
        self.pwmList = []
        for pin in pins:
            self.pwmList.append(PWMOut(pin, duty_cycle=0,frequency=5000))

    def setVals(self, arr):
        for i, pwm in enumerate(self.pwmList):
            pwm.duty_cycle = self.full-arr[i]*self.full

    def red(self):
        arr = (1, 0, 0)
        self.setVals(arr)

    def green(self):
        arr = (0, 1, 0)
        self.setVals(arr)  

    def blue(self):
        arr = (0, 0, 1)
        self.setVals(arr)  

    def magenta(self):
        arr = (1, 0, 1)
        self.setVals(arr)  

    def cyan(self):
        arr = (0, 1, 1)
        self.setVals(arr)  

    def yellow(self):
        arr = (1, 1, 0)
        self.setVals(arr)  

    def white(self):
        arr = (1, 1, 1)
        self.setVals(arr)  

    def black(self):
        arr = (0, 0, 0)
        self.setVals(arr)  

    def rainbow(self):
        print("rainbow")
        for i in range(self.full,0,-64):
            self.pwmList[0].duty_cycle = i
            sleep(.005)
        for i in range(self.full,0,-64):
            self.pwmList[1].duty_cycle = i
            self.pwmList[0].duty_cycle = self.full - i
            sleep(.005)
        for i in range(self.full,0,-64):
            self.pwmList[1].duty_cycle = self.full - i
            self.pwmList[2].duty_cycle = i
            sleep(.005)
        for i in range(self.full,0,-64):
            self.pwmList[0].duty_cycle = i
            sleep(.005)