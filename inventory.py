from menu import Menu

class Inventory():
    def __init__(self):
        self.menus=[]

    def addMenu(self, m):
        self.menus.append(m)

    def getMenus(self):
        return self.menus
    
    def getMenuByNumber(self, number):
        reqMenu=None
        for m in self.menus:
            if m.menunum==number:
                reqMenu=m
                break
        return reqMenu
