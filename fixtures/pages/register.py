import logging


from fixtures.locators.register import RegisterLocators
from fixtures.models.register import RegisterData
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class RegisterPage(BasePage):
    def add_new_user(self, data: RegisterData, is_submit: bool = True):
        """
        Register new user
        """
        logger.info(
            f"Register new user {data.login}, password {data.password}, "
            f"name {data.name}, city{data.city}"
        )
        self.fill_element(data=data.login, locator=RegisterLocators.LOGIN_INPUT)
        self.fill_element(data=data.password, locator=RegisterLocators.PASSWORD_INPUT)
        self.fill_element(data=data.email, locator=RegisterLocators.EMAIL_1)
        self.fill_element(data=data.email_2, locator=RegisterLocators.EMAIL_2)
        self.fill_element(data=data.name, locator=RegisterLocators.NAME)
        self.fill_element(data=data.surname, locator=RegisterLocators.SURNAME)
        self.fill_element(data=data.city, locator=RegisterLocators.CITY)
        if is_submit:
            self.click_element(locator=RegisterLocators.SUBMIT_BTN)

    def get_error_name(self) -> str:
        return self.get_text(locator=RegisterLocators.ERROR_FIRST_NAME)
