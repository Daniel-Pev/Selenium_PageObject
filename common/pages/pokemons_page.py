from loguru import logger
from selenium.webdriver.common.by import By

from common.pages.base_page import BasePage


class PokemonsPage(BasePage):
    """"
    Pokemons page class
    """

    def get_trainer_id(self):
        logger.info('Checking trainer ID')
        return self.find_element(locator=(By.CSS_SELECTOR, '[class*="text_type_profile"]')).text

    def get_headers(self):
        logger.info('Checking headers')
        return self.find_elements(locator=(By.CSS_SELECTOR, '.header__btn'))

    def pokemons_cards(self):
        logger.info('Checking amount of pokemons on page')
        return self.find_elements(locator=(By.CSS_SELECTOR, '.cards__link '))
