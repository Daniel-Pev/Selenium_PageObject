""""
Tests for my trainer page
"""

from common.conf import Cfg
from common.pages.my_trainer_page import MyTrainerPage


class TestMyTrainer:

    def test_open_url(self, driver):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        assert driver.current_url == f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}'

    def test_correct_headers(self, driver):
        trainer = MyTrainerPage(driver)
        headers = trainer.get_headers()
        assert [i.text for i in headers] == ['Покемоны', "Тренеры", "Рейтинг"], 'Unexpected header'

