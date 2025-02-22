""""
Tests for pokemons page
"""
import allure
from selenium.webdriver.common.by import By

from common.conf import Cfg
from common.pages.pokemons_page import PokemonsPage


@allure.suite('Pokemons page')
class TestPokemons:

    def test_open_url(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        assert driver.current_url == Cfg.URL + '/', 'Unexpected url'

    def test_trainer_id(self, driver, trainer_id=Cfg.TRAINER_ID):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        actual_id = pokemons.get_trainer_id()
        assert trainer_id == int(actual_id), 'Unexpected trainer ID'

    def test_correct_headers(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        headers = pokemons.get_headers()
        assert [i.text for i in headers] == ['Покемоны', "Тренеры", "Рейтинг"], 'Unexpected header'

    def test_title(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        assert 'Покемоны' == pokemons.get_title().text

    def test_pagination(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        pokemons_cards = pokemons.pokemons_cards()
        assert len(pokemons_cards) == 60, 'Unexpected amount of pokemons'

    @allure.sub_suite('Pokemons page filter')
    def test_filter_show_knockout(self, driver):
        is_displayed = False
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        pokemons.set_filter('knockout')
        pokemons_cards = pokemons.pokemons_cards()
        with allure.step('Checking that knocked out pokemons are displayed'):
            for card in pokemons_cards:
                if card.get_attribute('data-death') == 'true':
                    is_displayed = True
                    break
            assert is_displayed is True, "No knocked out pokemons displayed"

    def test_filter_in_pokeball(self, driver):
        pokemons = PokemonsPage(driver)
        pokemons.authorization()
        pokemons.set_filter('pokeball')
        with allure.step('Checking amount of pokemons in pokeball'):
            in_pokeball = pokemons.find_elements(locator=(By.CSS_SELECTOR, '[data-boll="true"]'))
        all_pokemons = pokemons.pokemons_cards()
        assert len(in_pokeball) == len(all_pokemons), 'Not all pokemons in pokeball'
