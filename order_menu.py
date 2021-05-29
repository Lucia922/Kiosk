from menu import menu
from kiosk import kiosk

class Order_menu():
    def __init__(self, order_menuid, kioskid, menuid, quantity):
        self.order_menuid=order_menuid
        self.kioskid=kioskid
        self.menuid=menuid
        self.quantity=quantity

    def getOrder_menuid(self):
        return self.order_menuid

    def getKioskID(self):
        return self.kioskid

    def getMenuID(self):
        return self.menuid

    def getQuantity(self):
        return self.quantity
        
    
