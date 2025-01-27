""""
Pokemons page class
"""
import allure
from loguru import logger
from selenium.webdriver.common.by import By

from common.pages.base_page import BasePage


class PokemonsPage(BasePage):

    def get_trainer_id(self):
        with allure.step('Checking trainer ID'):
            logger.info('Checking trainer ID')
            return self.find_element(locator=(By.CSS_SELECTOR, '[class*="text_type_profile"]')).text

    def get_headers(self):
        with allure.step('Checking headers'):
            logger.info('Checking headers')
            return self.find_elements(locator=(By.CSS_SELECTOR, '.header__btn'))

    def pokemons_cards(self):
        with allure.step('Checking amount of pokemons on page'):
            logger.info('Checking amount of pokemons on page')
            return self.find_elements(locator=(By.CSS_SELECTOR, '.cards__item'))

    def set_filter(self, filter):
        with allure.step(f'Setting filter {filter}'):
            logger.info(f'Setting filter {filter}')
            self.find_element(locator=(By.CSS_SELECTOR, '.pokemon__filter-btn')).click()
            if filter.lower() == 'pokeball':
                self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_has_pokeboll"] ~ .popup__fake')).click()
            elif filter.lower() == 'knockout':
                self.find_element(locator=(By.CSS_SELECTOR, '[class*="f_alive"] ~ .popup__fake')).click()
