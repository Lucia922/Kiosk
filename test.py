import unittest
from kiosk import Kiosk
from menu import Menu
from inventory import Inventory
from order_menu import Order_Menu
from order import Order
from payment import Payment

class KioskTest(unittest.TestCase):
    #set up an instance of the class
    def setUp(self): 
        self.kiosk=Kiosk(1, 1, 1, 1)
    #test the get methods
    def test_KioskId(self):
        self.assertEqual(self.kiosk.getKioskId(), 1)

    def test_PersonId(self):
        self.assertEqual(self.kiosk.getPersonId(), 1)

    def test_MenuId(self):
        self.assertEqual(self.kiosk.getMenuId(), 1)

    def test_LocationId(self):
        self.assertEqual(self.kiosk.getLocationId(), 1)

    # test class string method
    def test_kioskstring(self):
        self.assertEqual(str(self.kioskid), 1)
        
    def test_table(self):
        self.assertEqual(str(Kiosk._meta.db_table), 'kiosk')

 
class MenuTest(unittest.TestCase):
    def setUp(self):
        self.menu=Menu(1, 'macchiato', 2.25, 'espresso with a small amout of milk', 'coffee')

    def test_MenuId(self):
        self.assertEqual(self.menu.getMenuId(), 1)

    def test_Menu_Name(self):
        self.assertEqual(str(self.menu.getMenu_Nmae()), 'macchiato')

    def test_Menu_Price(self):
        self.assertEqual(str(self.menu.getMenu_Price()), 2.25)

    def test_Menu_Description(self):
        self.assertEqual(str(self.menu.getMenu_Description()), 'espresso with a small amout of milk')

    def test_Menu_Status(self):
        self.assertEqual(str(self.menu.getMenu_Status()), 'coffee')

    def test_menustring(self):
        self.assertEqual(str(self.menu_name), 'macchiato')

class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.menu1=Menu(1, 'macchiato', 2.25, 'espresso with a small amout of milk', 'coffee')
        self.menu2=Menu(2, 'hojitea', 3.00, 'rosted green tea', 'tea')
        self.menu3=Menu(3, 'aval', 3.75, 'french apple cider alcohol 6%', 'cider')

        #add menus
        self.inven=Inventory()
        self.inven.addMenu(self.menu1)
        self.inven.addMenu(self.menu2)
        self.inven.addMenu(self.menu3)

    def test_getMenus(self):
            
        menus=self.inven.getMenus()
        self.assertEqual(len(menus), 2)

    def test_getMenuByNumber(self):
        menu=self.inven.test_getMenuByNumber(3)
        self.assertEqual(str(menu), 'aval')

class Order_MenuTest(unittest.TestCase):
    def setUP(self):
        self.menu=menu(1, 'macchiato', 2.25, 'espresso with a small amout of milk', 'coffee')
        self.quantity=2
        self.order_menu=order_menu(self.menu, self.quantity)
        
    def test_getMenu(self):
        self.menu=self.order_menu.getMenu()
        self.assertEqual(str(self.menu), 'macchiato')

    def test_getMenuPriceFromOrderMenu(self):
        self.menu=self.order_menu.getMenu()
        self.assertEqual(self.menu.getMenu_Price(), 2.25)

    def test_getQuantity(self):
        self.assertEqual(self.order_menu.getQuantity)(), 2)

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.order=Order()
        self.menu1=Menu(1, 'macchiato', 2.25, 'espresso with a small amout of milk', 'coffee')
        self.menu2=Menu(2, 'hojitea', 3.00, 'rosted green tea', 'tea')
        self.menu3=Menu(3, 'aval', 3.75, 'french apple cider alcohol 6%', 'cider')
        self.order_date=Order(order_date=datetime.date(2021,6,3))
        self.order_status=Order(order_status='prepareing')
        self.promotion_codeid=Order(promotion_codeid=1)

        self.ordermenu1=Order_Menu(self.menu1, 1)
        self.ordermenu2=Order_Menu(self.menu2, 2)
        self.ordermenu3=Order_Menu(self.menu3, 2)

        self.order.addOrder_Menus(self.ordermenu1)
        self.order.addOrder_Menus(self.ordermenu2)
        self.order.addOrder_Menus(self.ordermenu3)

    def test_addOrder_Menus(self):
        self.order_menus=self.order.addOrder_Menus()
        self.assertEqual(len(self.order_menus), 3)

    def test_getOrer_Menus(self):
        self.order_menus=self.order.getOrder_Menus()
        self.assertEqual(len(self.order_menus), 3)

    def test_CalculateTotal(self):
        payment=self.order.calcTotal()
        self.assertEqual(str(payment), 'Your payent today will be 2.25')

    



    






        

