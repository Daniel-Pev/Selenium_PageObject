""""
Base Page class
"""

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.conf import Cfg


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = Cfg.URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except:
            return None

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def authorization(self):
        self.go_to_site()
        logger.info('Wait for clickable email input, type email')
        email = self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_email"]'))
        email.click()
        email.send_keys(Cfg.VALID['email'])

        logger.info('Wait for clickable password input, type password')
        password_field = self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_pass"]'))
        password_field.click()
        password_field.send_keys(Cfg.VALID['password'])

        logger.info('Click auth button')
        enter_button = self.find_element(locator=(By.CSS_SELECTOR, '[class*=send_auth'))
        enter_button.click()
        logger.info('Wait new url to load')
        try:
            return WebDriverWait(self.driver, timeout=10, poll_frequency=2).until(EC.url_to_be(f'{Cfg.URL}/'))
        except:
            logger.error(f'Failed to load {Cfg.URL}')
