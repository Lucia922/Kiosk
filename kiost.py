from menu import Menu
from person import Person
from location import location

class kiosk():
    def __init__(self, kioskid, personid, menuid, locationid):
        self.kioskid=kioskid
        self.personid=personid
        self.menuid=menuid
        self.locationid=locationid

    def getKioskId(self):
        return self.kioskid

    def getPersonID(self):
        return self.personid
    
    def getMenuId(self):
        return self.menuid

    def getLocationID(self):
        return self.locationid

    def __str__(self):
        return self.kioskid
     
