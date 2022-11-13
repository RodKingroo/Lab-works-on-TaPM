### Copyright (c) 2022 RodKingroo

class CeilingFan:
    def __init__(self):
        self.High = 3
        self.Medium = 2
        self.Low = 1
        self.Off = 0
        self.speed = self.Off

    def high(self):
        self.speed = self.High
        print('Ceiling Fan Speed', self.speed)

    def medium(self):
        self.speed = self.Medium
        print('Ceiling Fan Speed', self.speed)

    def low(self):
        self.speed = self.Low
        print('Ceiling Fan Speed', self.speed)

    def off(self):
        self.speed = self.off
        print('Ceiling Fan Speed', self.speed)

    def getSpeed(self):
        return self.speed
