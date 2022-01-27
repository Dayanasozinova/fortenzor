import pytest
from selenium import webdriver
@pytest.fixture(scope='session')  #функция выполниться только один раз за тестовую сессию
def browser():
    driver = webdriver.Chrome()
    yield driver  #разделяет функция на части до тестов и после тестов
    driver.quit()
