class ProductPage:

    def __init__(self, page):
        self.page = page

    def click_add_to_cart(self):
        self.page.locator("[data-test=\"add-to-cart\"]").click()