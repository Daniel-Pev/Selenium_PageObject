from common.conf import Cfg
from common.pages.pokemons_page import PokemonsPage


class TestPokemons:

    def test_open_url(self,driver):
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
