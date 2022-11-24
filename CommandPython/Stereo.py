# Copyright (c) 2022 RodKingroo

class Stereo:
    def __init__(self, ui):
        self.UNKNOWN = 0
        self.CASSETTE = 1
        self.CD = 2
        self.DVD = 3
        self.RADIO = 4
        self.CLOUDMUSIC = 5
        self.volume = 0
        self.state = self.UNKNOWN
        self.ui = ui
        
    def on(self):
        self.ui.set_text_output('Stereo On')
        
    def off(self):
        self.ui.set_text_output('Stereo Off')
    
    #setted cassete
    def setCASSETTE(self):
        self.state = self.CASSETTE
        self.ui.set_text_output('Cassette Rec selected')
    
    #setted CD
    def setCD(self):
        self.state = self.CD
        self.ui.set_text_output('CD device selected')
    
    #setted DVD
    def setDVD(self):
        self.state = self.DVD
        self.ui.set_text_output('DVD device selected')
        
    #setted Radio Example: play Radio Station
    def setRADIO(self):
        self.state = self.RADIO
        self.ui.set_text_output('Radio selected')
        
    # setted cloud music Example: Spotify, Yandex Music
    def setCLOUDMUSIC(self):
        self.state = self.CLOUDMUSIC
        self.ui.set_text_output('Voice Assist play music')
    
    def setVolume(self, volume):
        self.volume = volume
        self.ui.set_text_output("Volume level: " + str(self.volume))
        
    def getVolume(self):
        return self.volume
    
    def getState(self):
        return self.state
    