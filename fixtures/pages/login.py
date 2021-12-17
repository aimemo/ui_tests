import logging

from selenium.webdriver.common.by import By

from fixtures.locators.login import LoginLocators
from fixtures.models.login import LoginData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def auth(self, data: LoginData, is_submit: bool = True):
        """
        Auth func
        Если мы не login  → login
        Если мы login → logout → login
        """
        logger.info(f"Login with user {data.login} and password {data.password}")
        self.fill_element(data=data.login, locator=LoginLocators.LOGIN_INPUT)
        self.fill_element(data=data.password, locator=LoginLocators.PASSWORD_INPUT)
        if is_submit:
            self.click_element(locator=LoginLocators.LOGIN_BTN)

    def login_success(self):
        element = self.custom_find_element((By.ID, "action-menu-1-menubar"))
        return element.text

    def error(self):
        element = self.custom_find_element((By.ID, "loginerrormessage"))
        return element.text

    def _get_error_text(self) -> str:
        """
        Пример получения текста элемента!!!!
        """
        return self.get_text(locator=LoginLocators.LOGIN_BTN)
