from menu import Menu
from person import Person
from location import location

class kiosk():
    def __init__(self, kioskid, personid, menunum, locationid):
        self.kioskid=kioskid
        self.personid=personid
        self.menunum=menunum
        self.locationid=locationid

    #gets for fields
    def getKioskId(self):
        return self.kioskid

    def getPersonID(self):
        return self.personid
    
    def getMenuNum(self):
        return self.menunum

    def getLocationID(self):
        return self.locationid

    def __str__(self):
        return self.kioskid
     
