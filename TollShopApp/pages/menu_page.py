class MenuPage:

    def __init__(self, page):
        self.page = page
    
    def click_sign_in(self):
        self.page.locator("[data-test=\"nav-sign-in\"]").click() 
    
    def click_home(self):
        self.page.locator("[data-test=\"nav-home\"]").click()
    
    def get_cart_quantity(self):
        return self.page.locator("[data-test=\"cart-quantity\"]")
    
    def click_cart(self):
        self.page.locator("[data-test=\"nav-cart\"]").click() 

    
    