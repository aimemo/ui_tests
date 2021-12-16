from fixtures.pages.login import LoginPage
from fixtures.pages.register import RegisterPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.register = RegisterPage(self)

    def quit(self):
        self.driver.quit()

    def open_login_page(self):
        self.driver.get(self.url)

    def open_register_page(self):
        self.driver.get("https://qacoursemoodle.innopolis.university/login/signup.php?")
