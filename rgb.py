from pulseio import PWMOut #pylint: disable-msg=import-error
from time import sleep

class RGB:

    full = 2**16-1

    def __init__(self, r, g, b):
        self.r = PWMOut(r, frequency=5000, duty_cycle=0)
        self.g = PWMOut(g, frequency=5000, duty_cycle=0)
        self.b = PWMOut(b, frequency=5000, duty_cycle=0)

    def red(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = self.full
        self.b.duty_cycle = self.full

    def green(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def blue(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0

    def magenta(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0

    def cyan(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def yellow(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def white(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def black(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = self.full

    def rainbow(self):
        for i in range(self.full,0,-64):
            self.r.duty_cycle = i
            sleep(.005)
        for i in range(self.full,0,-64):
            self.g.duty_cycle = i
            self.r.duty_cycle = self.full - i
            sleep(.005)
        for i in range(self.full,0,-64):
            self.g.duty_cycle = self.full - i
            self.b.duty_cycle = i
            sleep(.005)