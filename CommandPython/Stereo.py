# Copyright (c) 2022 RodKingroo

class Stereo:
    def __init__(self):
        self.UNKNOWN = 0
        self.CASSETTE = 1
        self.CD = 2
        self.DVD = 3
        self.RADIO = 4
        self.CLOUDMUSIC = 5
        self.volume = 0
        self.state = self.UNKNOWN
        
    def on(self):
        print('Stereo On')
        
    def off(self):
        print('Stereo Off')
    
    #setted cassete
    def setCASSETTE(self):
        self.state = self.CASSETTE
        print('Cassette Rec selected')
    
    #setted CD
    def setCD(self):
        self.state = self.CD
        print('CD device selected')
    
    #setted DVD
    def setDVD(self):
        self.state = self.DVD
        print('DVD device selected')
        
    #setted Radio Example: play Radio Station
    def setRADIO(self):
        self.state = self.RADIO
        print('Radio selected')
        
    # setted cloud music Example: Spotify, Yandex Music
    def setCLOUDMUSIC(self):
        self.state = self.CLOUDMUSIC
        print('Voice Assist play music')
    
    def setVolume(self, volume):
        self.volume = volume
        print("Volume level:", self.volume)
        
    def getVolume(self):
        return self.volume
    
    def getState(self):
        return self.state
    