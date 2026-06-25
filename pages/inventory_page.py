class InventoryPage:
    def __init__(self,page):
        self.page=page
    def add_products(self):
        self.page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.page.click("#add-to-cart-sauce-labs-fleece-jacket")
    def open_cart(self):
        self.page.click(".shopping_cart_link")