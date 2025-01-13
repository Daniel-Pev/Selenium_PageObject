"""
Tests for login page
"""
import allure
import pytest
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.conf import Cfg
from common.pages.login_page import LoginPage


@allure.suite('Authorization')
@allure.sub_suite('Positive authorization')
class TestPositiveLogin:

    def test_successful_login(self, clear_report, driver):
        logger.info('AUTHORIZATION WITH VALID CREDS')
        login = LoginPage(driver=driver)
        login.authorization()
        assert driver.current_url == f'{login.base_url}/'

@allure.suite('Authorization')
@allure.sub_suite('Negative login')
class TestNegativeLogin:
    cases = [
        {'login': Cfg.VALID['email'], 'password': 'invalid_password'},
        {'login': 'invalid_email@111.222', 'password': Cfg.VALID['password']},
        {'login': 'invalid_email@111.222', 'password': 'invalid_password'},
        {'login': '11111@11.111', 'password': '#@$!#!#!#!$@!'},
        {'login': 'b@b.bb', 'password': 'a' * 251},
        {'login': 'b@b.bb', 'password': 'a'}
    ]

    @pytest.mark.parametrize('case', cases)
    def test_invalid_login(self, case, driver):
        logger.info('TRY TO AUTHORIZATION WITH INVALID EMAIL OR PASSWORD')
        login = LoginPage(driver)
        login.go_to_site()
        login.enter_login(login=case['login'])
        login.enter_password(password=case['password'])
        login.click_enter_button()
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, '[class*="error_text"]'))).text
        assert error_message == 'Неверные логин или пароль'

@allure.suite('Authorization')
@allure.sub_suite('Negative email validation')
class TestEmailValidation:
    cases = [
        {'login': '', 'password': 'invalid_password'},
        {'login': '%@!$!!@#@!#', 'password': Cfg.VALID['password']},
        {'login': 'sdmflskdmf@wkdmawda', 'password': 'invalid_password'},
        {'login': '1@1.1', 'password': '#@$!#!#!#!$@!'},
        {'login': '@1.11', 'password': '#@$!#!#!#!$@!'},
        {'login': '#@1.11', 'password': '#@$!#!#!#!$@!'}
    ]

    @pytest.mark.parametrize('case', cases)
    def test_invalid_email(self, case, driver):
        logger.info('CHECKING EMAIL FIELD VALIDATION')
        login = LoginPage(driver)
        login.go_to_site()
        login.enter_login(login=case['login'])
        login.enter_password(password=case['password'])
        login.click_enter_button()
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, '.auth__error'))).text
        assert error_message == 'Введите почту'
