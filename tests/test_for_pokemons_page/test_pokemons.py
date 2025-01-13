""""
Tests for pokemons page
"""

from selenium.webdriver.common.by import By
from common.conf import Cfg
from common.pages.pokemons_page import PokemonsPage


class TestPokemons:

    def test_open_url(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        assert driver.current_url == Cfg.URL + '/', 'Unexpected url'

    def test_trainer_id(self, driver, trainer_id=Cfg.TRAINER_ID):
        pokemon = PokemonsPage(driver)
        assert trainer_id == int(pokemon.get_trainer_id()), 'Unexpected trainer ID'

    def test_correct_headers(self, driver):
        pokemons = PokemonsPage(driver)
        headers = pokemons.get_headers()
        assert [i.text for i in headers] == ['Покемоны', "Тренеры", "Рейтинг"], 'Unexpected header'

    def test_pagination(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons_cards = pokemons.pokemons_cards()
        assert len(pokemons_cards) == 60, 'Unexpected amount of pokemons'


def test_filter_show_knockout(driver):
    is_displayed = False
    pokemons = PokemonsPage(driver)
    pokemons.authorization()
    pokemons.find_element(locator=(By.CSS_SELECTOR, '.pokemon__filter-btn')).click()
    pokemons.find_element(locator=(By.CSS_SELECTOR, '[class*="f_alive"] ~ .popup__fake')).click()
    pokemons_cards = pokemons.pokemons_cards()
    for card in pokemons_cards:
        if card.get_attribute('data-death') == 'true':
            is_displayed = True
            break
    assert is_displayed is True, "No knocked out pokemons displayed"


def test_filter_in_pokeball(driver):
    pokemons = PokemonsPage(driver)
    pokemons.authorization()
    pokemons.find_element(locator=(By.CSS_SELECTOR, '.pokemon__filter-btn')).click()
    pokemons.find_element(locator=(By.CSS_SELECTOR, '[class*="f_has_pokeboll"] ~ .popup__fake')).click()
    in_pokeball = pokemons.find_elements(locator=(By.CSS_SELECTOR, '[data-boll="true"]'))
    all_pokemons = pokemons.pokemons_cards()
    assert len(in_pokeball) == len(all_pokemons), 'Not all pokemons in pokeball'
