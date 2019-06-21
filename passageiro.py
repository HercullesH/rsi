class Passageiro:
    def __init__(self):
        self.mac = ""
        self.currentTime = 0
        self.lastTime = 0
        self.firstLatitude = 0
        self.firstLongitude = 0
        self.lastLatitude = 0
        self.lastLongitude = 0
        self.rssi = 0
        self.firsTime = 0
        self.speed = 0
        self.situacao = False
     
    def setMac(self, mac):
        self.mac = mac
    
    def setFirstTime(self, firsTime):
        self.firsTime = firsTime
    
    def setRssi(self, rssi):
        self.rssi = rssi
     
    def setLastTime(self, lastTime):
        self.lastTime = lastTime

    def setFirstLatitude(self, latitude):
        self.firstLatitude = latitude
    
    def setCurrentTime(self, currentTime):
        self.currentTime = currentTime
    
    def setFirstLongitude(self, longitude):
        self.firstLongitude = longitude

    def setLastLongitude(self, longitude):
        self.lastLongitude = longitude
    
    def setLastLatitude(self, latitude):
        self.lastLatitude = latitude
    
    def setSpeed(self,speed):
        self.speed = speed
    
    def setSituacao(self,situacao):
        self.situacao = situacao



     
    def getMac(self):
        return self.mac

    def getSpeed(self):
        return self.speed

    def getRssi(self):
        return self.rssi
         
    def getCurrentTime(self):
        return self.currentTime
    
    def getLastTime(self):
        return self.lastTime
    
    def getFirstLatitude(self):
        return self.firstLatitude
    
    def getFirstLongitude(self):
        return self.firstLongitude
    
    def getFirstTime(self):
        return self.firsTime

    def getLastLatitude(self):
        return self.lastLatitude
    
    def getLastLongitude(self):
        return self.lastLongitude
    
    def getSituacao(self):
        return self.situacao




