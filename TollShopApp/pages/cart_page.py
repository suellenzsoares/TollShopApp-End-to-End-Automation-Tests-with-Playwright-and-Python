class CartPage:

    def __init__(self, page):
        self.page = page
    
    def get_line_price(self):
        return self.page.locator("[data-test=\"line-price\"]")
    
    def get_cart_total(self):
        return self.page.locator("[data-test=\"cart-total\"]")
    
    def click_proceed_to_checkout_button(self):
        self.page.locator('[data-test^="proceed-"]:visible').click()

    def flow_proceed_to_checkout(self):
        self.click_proceed_to_checkout_button()
        self.click_proceed_to_checkout_button()