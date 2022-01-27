from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver    #инициализируем драйвер
        self.base_url = "https://yandex.ru/"    #указываем url для открытия страницы

    def find_element(self, locator, time=10):   #ищет один элемент и возвращает его
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10): #ищет множество элементов и возвращает список
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    #WebDriverWait отвечает за явные ожидания в Selenium

    def go_to_site(self): #переходим на указанную в base_url страницу
        return self.driver.get(self.base_url)
