""""
Tests for my trainer page
"""
import allure

from common.conf import Cfg
from common.pages.trainer_page import MyTrainerPage


@allure.suite('Trainer Page')
class TestTrainer:

    def test_open_url(self, driver):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        assert driver.current_url == f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}', '"Unexpected url"'

    def test_correct_headers(self, driver):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        headers = trainer.get_headers()
        assert [i.text for i in headers] == ['Покемоны', "Тренеры", "Рейтинг"], 'Unexpected header'
