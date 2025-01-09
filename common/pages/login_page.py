""""
Login page class
"""

from loguru import logger
from selenium.webdriver.common.by import By
from common.conf import Cfg
from common.pages.base_page import BasePage


class LoginPage(BasePage):

    def enter_login(self, login=None):
        if login is None:
            login = Cfg.VALID['email']
        logger.info('Wait for clickable email input, type email')
        email = self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_email"]'))
        email.click()
        email.send_keys(login)

    def enter_password(self, password=None):
        if password is None:
            password = Cfg.VALID['password']
        logger.info('Wait for clickable password input, type password')
        password_field = self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_pass"]'))
        password_field.click()
        password_field.send_keys(password)

    def click_enter_button(self):
        logger.info('Click auth button')
        enter_button = self.find_element(locator=(By.CSS_SELECTOR, '[class*=send_auth'))
        enter_button.click()
