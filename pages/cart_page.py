class CartPage:
    def __init__(self,page):
        self.page=page
    def verify_products(self):
        items=self.page.locator(".inventory_item_name").all_inner_texts()

        assert "Sauce Labs Bolt T-Shirt" in items
        assert "Sauce Labs Fleece Jacket" in items
    def click_checkout(self):
        self.page.click("#checkout")
