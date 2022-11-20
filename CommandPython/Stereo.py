class Stereo:
    def __init__(self):
        self.UNKNOWN = 0
        self.CD = 1
        self.volume = 0
        self.state = self.RADIO
        
    def on(self):
        print('Stereo On')
        
    def off(self):
        print('Stereo On')
    
    def setCD(self):
        print('CD set')
    
    def setVolume(self, volume):
        self.volume = volume
        
    def getVolume(self):
        return self.volume
    
    def getState(self):
        return self.state
    