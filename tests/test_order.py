from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage

def test_place_order(page):
    login=LoginPage(page)
    inventory=InventoryPage(page)
    cart=CartPage(page)
    checkout=CheckoutPage(page)
    complete=CompletePage(page)

    login.navigate()
    username,password=login.get_credentials()
    login.login(username,password)

    inventory.add_products()
    inventory.open_cart()

    cart.verify_products()
    cart.click_checkout()

    checkout.enter_customer_details(
        "Dibya",
        "Chuli",
        "411001"
    )

    checkout.verify_total_price()
    checkout.finish_order()

    complete.verify_success_message()