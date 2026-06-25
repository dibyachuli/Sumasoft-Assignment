class CheckoutPage:
    def __init__(self, page):
        self.page = page
    def enter_customer_details(self,first,last,postal):
        self.page.fill("#first-name",first)
        self.page.fill("#last-name",last)
        self.page.fill("#postal-code",postal)
        self.page.click("#continue")
    def verify_total_price(self):
        prices=self.page.locator(".inventory_item_price").all_inner_texts()
        tshirt_price=float(prices[0].replace("$",""))
        jacket_price = float(prices[1].replace("$", ""))
        item_total=tshirt_price+jacket_price
        total_text=self.page.locator(".summary_total_label").inner_text()
        total_price=float(total_text.split("$")[1])

        assert total_price>item_total
    def finish_order(self):
        self.page.click("#finish")