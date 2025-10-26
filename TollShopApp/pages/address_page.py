class AddressPage:

    def __init__(self, page):
        self.page = page

    def fill_street(self, street):
        self.page.locator("[data-test=\"street\"]").clear()
        self.page.locator("[data-test=\"street\"]").fill(street)    

    def fill_city(self, city):
        self.page.locator("[data-test=\"city\"]").clear()
        self.page.locator("[data-test=\"city\"]").fill(city)    
    
    def fill_state(self, state):
        self.page.locator("[data-test=\"state\"]").clear()
        self.page.locator("[data-test=\"state\"]").fill(state)

    def fill_country(self, country):
        self.page.locator("[data-test=\"country\"]").clear()
        self.page.locator("[data-test=\"country\"]").fill(country)  
    
    def fill_postal_code(self, postal_code):
        self.page.locator("[data-test=\"postal_code\"]").clear()
        self.page.locator("[data-test=\"postal_code\"]").fill(postal_code)

    def click_proceed_button(self):
        self.page.locator('[data-test^="proceed-"]:visible').click()

    def fill_address_form(self, street, city, state, country, postal_code):
        self.fill_street(street)
        self.fill_city(city)
        self.fill_state(state)
        self.fill_country(country)
        self.fill_postal_code(postal_code)
        self.click_proceed_button()