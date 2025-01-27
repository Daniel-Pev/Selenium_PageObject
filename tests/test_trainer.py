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

    def test_trainer_name(self, driver, trainer_name=Cfg.TRAINER_NAME):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        actual_name = trainer.get_trainer_name()
        assert actual_name == trainer_name, 'Unexpected trainer name'

    def test_trainer_id(self, driver, trainer_id=Cfg.TRAINER_ID):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        actual_id = trainer.get_trainer_id()
        assert trainer_id == int(actual_id), 'Unexpected trainer ID'

    def test_trainer_city(self, driver, trainer_city=Cfg.TRAINER_CITY):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        actual_city = trainer.get_trainer_city()
        assert actual_city == trainer_city, 'Unexpected trainer city'

    def test_export_button_is_clickable(self, driver):
        trainer = MyTrainerPage(driver)
        trainer.authorization()
        trainer.go_to_site(url=f'{Cfg.URL}/trainer/{Cfg.TRAINER_ID}')
        with allure.step('Checking export button is clickable'):
            assert trainer.find_export_button().is_displayed()



