class SearchedProductsPage:

    def __init__(self, page):
        self.page = page

    def verify_search_term(self):
        return self.page.locator("[data-test=\"search-term\"]")
    
    def select_product_from_results(self, product_name):
        self.page.locator('a[data-test^="product-"]').filter(has_text=product_name).click()