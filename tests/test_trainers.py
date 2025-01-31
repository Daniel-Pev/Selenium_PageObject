""""
Tests for trainers page
"""
import allure
import pytest
from selenium.webdriver.common.by import By

from common.conf import Cfg
from common.pages.trainers_page import TrainersPage


@allure.suite('Trainers page')
class TestTrainers:

    def test_open_url(self, driver):
        trainers = TrainersPage(driver)
        trainers.authorization()
        trainers.go_to_site(url=f'{Cfg.URL}/trainers')
        assert driver.current_url == f'{Cfg.URL}/trainers', 'Unexpected url'

    def test_trainer_id(self, driver, trainer_id=Cfg.TRAINER_ID):
        trainers = TrainersPage(driver)
        trainers.authorization()
        trainers.go_to_site(url=f'{Cfg.URL}/trainers')
        actual_id = trainers.get_trainer_id()
        assert trainer_id == int(actual_id), 'Unexpected trainer ID'

    def test_correct_headers(self, driver):
        trainers = TrainersPage(driver)
        trainers.authorization()
        trainers.go_to_site(url=f'{Cfg.URL}/trainers')
        headers = trainers.get_headers()
        assert [i.text for i in headers] == ['Покемоны', "Тренеры", "Рейтинг"], 'Unexpected header'

    def test_title(self, driver):
        trainers = TrainersPage(driver)
        trainers.authorization()
        trainers.go_to_site(url=f'{Cfg.URL}/trainers')
        assert 'Тренеры' == trainers.get_title().text

    def test_pagination(self, driver):
        trainers = TrainersPage(driver)
        trainers.authorization()
        trainers.go_to_site(url=f'{Cfg.URL}/trainers')
        trainers_cards = trainers.trainers_cards()
        assert len(trainers_cards) == 60, 'Unexpected amount of trainers'

    level_cases = [i for i in range(1, 6)]

    @allure.sub_suite('Trainers page filter')
    @pytest.mark.parametrize('level', level_cases)
    def test_attack_filter(self, level, driver):
        trainers = TrainersPage(driver)
        trainers.authorization()
        trainers.go_to_site(url=f'{Cfg.URL}/trainers')
        trainers.set_filter(level)
        with allure.step('Checking trainers attack'):
            correct_level = trainers.find_elements(locator=(By.CSS_SELECTOR, f'.level__name[data-level="{level}"]'))
        all_trainers = trainers.trainers_cards()
        assert len(correct_level) == len(all_trainers), 'Not all trainers has correct level'
