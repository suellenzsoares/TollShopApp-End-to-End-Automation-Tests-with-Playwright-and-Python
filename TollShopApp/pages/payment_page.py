class PaymentPage:

    def __init__(self, page):
        self.page = page

    def select_payment_method(self, method):
        self.page.locator("[data-test=\"payment-method\"]").select_option(method)
    
    def fill_credit_card_number(self, number):
        self.page.locator("[data-test=\"credit_card_number\"]").fill(number)

    def fill_expiration_date(self, date):
        self.page.locator("[data-test=\"expiration_date\"]").fill(date)

    def fill_cvv(self, cvv):
        self.page.locator("[data-test=\"cvv\"]").fill(cvv)

    def fill_card_holder_name(self, name):
        self.page.locator("[data-test=\"card_holder_name\"]").fill(name)

    def click_finish_button(self):
        self.page.locator("[data-test=\"finish\"]").click()   

    def fill_complete_payment_data(self, method, number, date, cvv, name):
        self.select_payment_method(method)
        self.fill_credit_card_number(number)
        self.fill_expiration_date(date)
        self.fill_cvv(cvv)
        self.fill_card_holder_name(name)
        self.click_finish_button()     

    def get_payment_success_message(self):
        return self.page.locator("[data-test=\"payment-success-message\"]")
    
    def get_payment_order_confirmation(self):
        return self.page.locator("#order-confirmation")
   