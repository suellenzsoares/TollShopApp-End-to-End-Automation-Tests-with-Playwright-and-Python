class SideMenuPage:

    def __init__(self, page):
        self.page = page
    
    def fill_search_field(self, search_term):
        self.page.locator("[data-test=\"search-query\"]").fill(search_term)
    
    def click_search_button(self):
        self.page.locator("[data-test=\"search-submit\"]").click()
    
    def search_flow(self, search_term):
        self.fill_search_field(search_term)
        self.click_search_button()