from menu import Menu
from order_menu import order_menu
from payment import payment

class Order():
    def __init__(self, orderid, order_menuid, order_date, order_status, promotion_codeid):
        self.orderid=orderid
        self.order_menuid=[]
        self.order_date=datetime.order_date.today()
        self.order_time=datetime.order_time.strftime()
        self.order_status=order_status
        self.promotion_codeid=promotion_codeid

    def getOrderId(self):
        return self.orderid

    def addOrder_menuid(self, order_menuid):
        self.order_menuid.append(order_menuid)

    def getOrder_menuid(self):
        return self.order_menuid

    def getOrder_date(self):
        return self.order_date

    def getOrder_time(self):
        return self.order_time

    def getOrder_status(self):
        return self.order_status

    def getPromotion_codeid(self):
        return self.promotion_codeid

    def calcTotal(self):
        total=0.0
        for o in self.order_menuid:
            total += 0.getMenu().menu_price * 0.quantity
            payment=Payment(total)
        return payment

        