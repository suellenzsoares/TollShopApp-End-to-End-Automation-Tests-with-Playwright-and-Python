import re
from playwright.sync_api import Playwright, sync_playwright, expect
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.side_menu_page import SideMenuPage
from pages.searched_products_page import SearchedProductsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.address_page import AddressPage
from pages.payment_page import PaymentPage
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../.env')

BASE_URL = os.getenv('BASE_URL')
USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')


def test_purchase_products(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    menu_page = MenuPage(page)
    side_menu_page = SideMenuPage(page)
    searched_products_page = SearchedProductsPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    address_page = AddressPage(page)    
    payment_page = PaymentPage(page)
    

    # Go to https://practicesoftwaretesting.com/
    page.goto(BASE_URL)

    menu_page.click_sign_in()
    login_page.login_flow(USER_EMAIL, USER_PASSWORD)

    page.wait_for_url("**/account")
    menu_page.click_home()

    side_menu_page.search_flow("Thor Hammer")

    expect(searched_products_page.verify_search_term()).to_contain_text("Thor Hammer")
    searched_products_page.select_product_from_results("Thor Hammer")
    
    product_page.click_add_to_cart()
    expect(menu_page.get_cart_quantity()).to_contain_text("1") 
    
    menu_page.click_cart()
    
    expect(cart_page.get_line_price()).to_contain_text("$11.14") 
    expect(cart_page.get_cart_total()).to_contain_text("$11.14") 

    cart_page.flow_proceed_to_checkout()   
    
    address_page.fill_address_form("Test street 98", "Vienna", "Bundesland", "Austria", "1020")

    payment_page.fill_complete_payment_data("Credit Card", "0000-0000-0000-0000", "10/2028", "123", "Jack Howe")
    
    expect(payment_page.get_payment_success_message()).to_contain_text("Payment was successful")
    payment_page.click_finish_button()


    expect(payment_page.get_payment_order_confirmation()).to_contain_text("Thanks for your order! Your invoice number is ")

    context.close()
    browser.close()


