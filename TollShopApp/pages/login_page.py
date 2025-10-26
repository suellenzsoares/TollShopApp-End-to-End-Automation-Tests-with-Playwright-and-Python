class LoginPage:

    def __init__(self, page):
        self.page = page

    def fill_email(self, email):
        self.page.locator("[data-test=\"email\"]").fill(email)

    def fill_password(self, password):
        self.page.locator("[data-test=\"password\"]").fill(password)

    def click_login_button(self):
        self. page.locator("[data-test=\"login-submit\"]").focus()
        self.page.locator("[data-test=\"login-submit\"]").click()
    
    def login_flow(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()


         
    
   