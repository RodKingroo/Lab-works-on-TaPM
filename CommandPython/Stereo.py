### Copyright (c) 2022 RodKingroo

class Stereo:
    def __init__(self):
        self.CD = 0
        self.DVD = 1
        self.Radio = 2
        self.volume = 0
        self.state = self.Radio

    def on(self):
        print('Stereo On')

    def off(self):
        print('Stereo Off')

    def setCD(self):
        print('CD set')

    def setDVD(self):
        print('DVD set');

    def setRadio(self):
        print('Radio set')

    def setVolume(self, volume):
        self.volume = volume

    def getVolume(self):
        return self.volume

    def getState(self):
        return self.state






