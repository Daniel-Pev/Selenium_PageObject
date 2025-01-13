"""
Configuration file
"""
import os
import pytest
from loguru import logger


@pytest.fixture(scope="session", autouse=True)
def clear_report():
    """"
    Clear allure report
    """
    path = 'C:\\PythonProjects\\pokemon_PageObject\\results'
    for file_name in os.listdir(path):
        file = path + '\\' + file_name
        logger.info(f'Deleting file: {file_name}')
        os.remove(file)


