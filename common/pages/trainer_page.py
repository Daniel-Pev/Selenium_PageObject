""""
My trainer page class
"""

from loguru import logger
from selenium.webdriver.common.by import By
import allure
from common.pages.base_page import BasePage


class MyTrainerPage(BasePage):

    def get_trainer_id(self):
        with allure.step('Checking trainer ID'):
            logger.info('Checking trainer ID')
            return self.find_element(locator=(By.CSS_SELECTOR, '[class*="text_type_profile"]')).text

    def get_headers(self):
        with allure.step('Checking headers'):
            logger.info('Checking headers')
            return self.find_elements(locator=(By.CSS_SELECTOR, '.header__btn'))

    def get_trainer_name(self):
        with allure.step('Checking trainer name'):
            logger.info('Checking trainer name')
        return self.find_element(locator=(By.CSS_SELECTOR, '[class*="trainer_name"]')).text

    def get_trainer_city(self):
        with allure.step('Checking trainer city'):
            logger.info('Checking trainer city')
        return self.find_element(locator=(By.CSS_SELECTOR, '[class*="trainer_city"]')).text

    def find_export_button(self):
        logger.info('Checking export button')
        return self.find_element(locator=(By.CSS_SELECTOR, '.export__button_border'))
