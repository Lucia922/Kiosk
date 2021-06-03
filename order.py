from menu import Menu
from order_menu import order_menu
from payment import payment

class Order():
    def __init__(self, order_menu, order_date, order_status, promotion_codeid):
        self.order_menu=[]
        self.order_date=datetime.order_date.today()
        self.order_time=datetime.order_time.strftime()
        self.order_status=order_status
        self.promotion_codeid=promotion_codeid

    def addOrder_menus(self, menunum):
        self.order_menus.append(order_menu)

    def getOrder_menus(self):
        return self.order_menu

    def getOrder_date(self):
        return self.order_date

    def getOrder_status(self):
        return self.order_status

    def getPromotion_codeid(self):
        return self.promotion_codeid

    def calcTotal(self):
        total=0.0
        for o in self.order_menunum:
            total += 0.getMenu().menu_price * 0.quantity
            payment=Payment(total)
        return payment

        