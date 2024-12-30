from loguru import logger
from selenium.webdriver.common.by import By
from common.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.conf import Cfg

class LoginPage(BasePage):
    """"
    Login page class
    """
    def authorization(self):

        logger.info('Wait for clickable email input, type email')
        email = WebDriverWait(self.driver, timeout=10, poll_frequency=2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class*="f_email"]')))
        email.click()
        email.send_keys(Cfg.VALID['email'])

        logger.info('Wait for clickable password input, type password')
        password = self.driver.find_element(by=By.CSS_SELECTOR, value='[class*="f_pass"]')
        password.click()
        password.send_keys(Cfg.VALID['password'])

        logger.info('Press Enter to login')
        enter = self.driver.find_element(by=By.CSS_SELECTOR, value='[class*="send_auth"]')
        enter.click()

        logger.info('Wait new url to load')
        try:
            WebDriverWait(self.driver, timeout=10, poll_frequency=2).until(EC.url_to_be(f'{Cfg.URL}/'))
        except:
            logger.error(f'Failed to load {Cfg.URL}')
