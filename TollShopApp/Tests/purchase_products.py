# Required imports for the test
from playwright.sync_api import Playwright, sync_playwright, expect
# Imports Page Object classes to interact with different parts of the application
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.side_menu_page import SideMenuPage
from pages.searched_products_page import SearchedProductsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.address_page import AddressPage
from pages.payment_page import PaymentPage
# Imports modules to load environment variables
from dotenv import load_dotenv
import os

# Loads environment variables from the .env file
load_dotenv(dotenv_path='../.env')

# Retrieves environment variables
BASE_URL = os.getenv('BASE_URL')
USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')
CARD_NUMBER = os.getenv('CARD_NUMBER')
CARD_EXPIRY = os.getenv('CARD_EXPIRY')
CARD_CVV = os.getenv('CARD_CVV')
CARD_NAME = os.getenv('CARD_NAME')


def test_purchase_products(playwright: Playwright) -> None:
    """Tests the complete product purchase flow in the TollShopApp application."""
    # Configures the Chromium browser for the test (add headless=False for visualization)
    browser = playwright.chromium.launch()
    # Creates a new browser context
    context = browser.new_context()
    # Creates a new page in the context
    page = context.new_page()

    # Instantiates Page Object classes for each part of the application
    login_page = LoginPage(page)
    menu_page = MenuPage(page)
    side_menu_page = SideMenuPage(page) 
    page.wait_for_selector('[data-test="nav-sign-in"]', timeout=30000)   
    print("BASE_URL:", BASE_URL)
    page.screenshot(path="screenshot_before_sign_in.png")    
    menu_page.click_sign_in()
    searched_products_page = SearchedProductsPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    address_page = AddressPage(page)    
    payment_page = PaymentPage(page)

    # Defines the product to be searched
    product = "Thor Hammer"    

    # Navigates to the base URL of the application
    page.goto(BASE_URL)

    # Login flow
    menu_page.click_sign_in()
    login_page.login_flow(USER_EMAIL, USER_PASSWORD)

    # Waits for the account URL to load after login
    page.wait_for_url("**/account")
    # Returns to the home page
    menu_page.click_home()

    # Product search flow
    side_menu_page.search_flow(product)

    # Verifies if the search term is present in the results
    expect(searched_products_page.verify_search_term()).to_contain_text(product)
    # Selects the product from the search results
    searched_products_page.select_product_from_results(product)
    
    # Adds the product to the cart
    product_page.click_add_to_cart()
    # Verifies if the cart quantity is 1
    expect(menu_page.get_cart_quantity()).to_contain_text("1") 
    
    # Clicks on the cart icon
    menu_page.click_cart()
    
    # Verifies the line price and cart total
    expect(cart_page.get_line_price()).to_contain_text("$11.14") 
    expect(cart_page.get_cart_total()).to_contain_text("$11.14") 

    # Proceeds to checkout
    cart_page.flow_proceed_to_checkout()   
    
    # Fills the address form
    address_page.fill_address_form("Test street 98", "Vienna", "Bundesland", "Austria", "1020")

    # Fills payment details using environment variables
    payment_page.fill_complete_payment_data("Credit Card", CARD_NUMBER, CARD_EXPIRY, CARD_CVV, CARD_NAME)
    
    # Verifies the payment success message
    expect(payment_page.get_payment_success_message()).to_contain_text("Payment was successful")
    # Clicks the finish button
    payment_page.click_finish_button()


    # Verifies the order confirmation message
    expect(payment_page.get_payment_order_confirmation()).to_contain_text("Thanks for your order! Your invoice number is ")

    # Closes the browser context and the browser
    context.close()
    browser.close()


