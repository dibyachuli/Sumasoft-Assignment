class LoginPage:
    def __init__(self,page):
        self.page=page
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
    def get_credentials(self):
        username=self.page.locator("#login_credentials").inner_text()
        password = self.page.locator(".login_password").inner_text()
        user=username.split("\n")[1]
        pwd=password.split("\n")[1]
        return user,pwd
    def login(self,username,password):
        self.page.fill("#user-name",username)
        self.page.fill("#password",password)
        self.page.click("#login-button")