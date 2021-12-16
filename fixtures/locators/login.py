from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginbtn")
