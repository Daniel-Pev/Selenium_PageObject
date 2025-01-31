""""
Trainers page class
"""
import allure
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.pages.base_page import BasePage


class TrainersPage(BasePage):

    def get_trainer_id(self):
        with allure.step('Checking trainer ID'):
            logger.info('Checking trainer ID')
            return self.find_element(locator=(By.CSS_SELECTOR, '[class*="text_type_profile"]')).text

    def get_headers(self):
        with (allure.step('Checking headers')):
            logger.info('Checking headers')
            WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.header__btn')))
        return self.find_elements(locator=(By.CSS_SELECTOR, '.header__btn'))

    def trainers_cards(self):
        with allure.step('Checking amount of trainers on page'):
            logger.info('Checking amount of trainers on page')
            return self.find_elements(locator=(By.CSS_SELECTOR, '.trainers__link'))

    def set_filter(self, filter):
        with allure.step(f'Setting filter to {filter} level'):
            logger.info(f'Setting filter to {filter} level')
            self.find_element(locator=(By.CSS_SELECTOR, '.pokemon__filter-btn')).click()
            self.find_element(locator=(By.CSS_SELECTOR, f'.filter__label [value="{filter}"]~.filter__span')).click()

    def get_title(self):
        return self.find_element(locator=(By.CSS_SELECTOR, '.pokemon__title'))
