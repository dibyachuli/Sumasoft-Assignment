class CompletePage:
    def __init__(self, page):
        self.page = page
    def verify_success_message(self):
        message=self.page.locator(".complete-header").inner_text()

        assert message=="Thank you for your order!"
