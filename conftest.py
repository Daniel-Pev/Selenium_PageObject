"""
Configuration file
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    """
    Main fixture
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")  # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars")  # disabling infobars
    chrome_options.add_argument("--disable-extensions")  # disabling extensions
    chrome_options.add_argument("--disable-gpu")  # applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--headless")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
