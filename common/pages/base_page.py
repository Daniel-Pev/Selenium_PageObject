""""
Base Page class
"""
import allure
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.conf import Cfg


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = Cfg.URL

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=15):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except:
            return None

    def go_to_site(self, url=None):

        if url is None:
            url = self.base_url
        with allure.step(f'Opening {url}'):
            logger.info(f'Opening {url}')
            return self.driver.get(url)


    def authorization(self):
        with allure.step(f'Authorization on {Cfg.URL} '):
            self.go_to_site()
            with allure.step('Input login'):
                logger.info('Wait for clickable email input, type email')
                email = self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_email"]'))
                email.click()
                email.send_keys(Cfg.VALID['email'])
            with allure.step('Input login'):
                logger.info('Wait for clickable password input, type password')
                password_field = self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_pass"]'))
                password_field.click()
                password_field.send_keys(Cfg.VALID['password'])

            with allure.step('Click auth button'):
                logger.info('Click auth button')
                enter_button = self.find_element(locator=(By.CSS_SELECTOR, '[class*=send_auth'))
                enter_button.click()
                logger.info('Wait new url to load')
                try:
                    return WebDriverWait(self.driver, timeout=15, poll_frequency=2).until(EC.url_to_be(f'{Cfg.URL}/'))
                except:
                    logger.error(f'Failed to load {Cfg.URL}')
