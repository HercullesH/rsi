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
        self.negativo = 0
        self.positivo = False
        self.lastRssi = 0
     
    def setMac(self, mac):
        self.mac = mac
    
    def setFirstTime(self, firsTime):
        self.firsTime = firsTime
    
    def setLastRssi(self, lastRssi):
        self.lastRssi = lastRssi

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
    
    def setNegativo(self,negativo):
        self.negativo = negativo
    
    def setPositivo(self,positivo):
        self.positivo = positivo



     
    def getMac(self):
        return self.mac

    def getNegativo(self):
        return self.negativo

    def getRssi(self):
        return self.rssi
    
    def getLastRssi(self):
        return self.lastRssi
         
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
    
    def getPositivo(self):
        return self.positivo




