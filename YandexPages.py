from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



class YandexSearchLocators:  # класс для хронения локаторов
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")  # локатор поисковой строки
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")  # локатор кнопки "Найти"
    LOCATOR_YANDEX_SEARCH_SUGGEST_BAR = (By.CLASS_NAME, "mini-suggest__popup-content")  # локатор таблицы с подсказками
    LOCATOR_YANDEX_SEARCH_LINKS = (By.TAG_NAME, "a")  # поиск результатов поиска
    LOCATOR_YANDEX_SEARCH_LINK_PAGES = (By.LINK_TEXT, "Картинки")
    LOCATOR_YANDEX_SEARCH_POPULAR_REQUEST_LIST = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a")
    LOCATOR_YANDEX_SEARCH_INPUT_CONTROL = (By.CLASS_NAME, "input__control")
    LOCATOR_YANDEX_SEARCH_FIRST_PAGES = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a")
    LOCATOR_YANDEX_SEARCH_BUTTON_NEXT_PAGE = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_YANDEX_SEARCH_BUTTON_BACK_PAGE = (By.CLASS_NAME, 'CircleButton')



class SearchHelper(BasePage):
    def check_search_field(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def enter_word(self, word):  # ищет поисковыую строку,кликает не нее, вводит слово
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):  # ищет элемент кнопки "Найти" и кликает на нее
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def check_suggest_bar(self):  # ищет элемент таблицы с подсказками
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SUGGEST_BAR)

    def check_link_in_table_result(self):
        links = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINKS)
        link_list = []
        i = 0
        for link in links:
            link_list.append(str(link.get_attribute("href")))
        link_list.remove('None')
        for l in link_list:
            if 'tensor.ru' in l:
                i += 1

        assert i >= 5

    def check_link_pages_in_site(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINK_PAGES)

    def click_on_link_pages(self):
        self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINK_PAGES).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def check_location_pages(self):
        assert "https://yandex.ru/images/" in self.driver.current_url

    def open_first_category_and_check(self):
        element = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_POPULAR_REQUEST_LIST)
        element.click()
        assert element.get_attribute("href") == self.driver.current_url
        input_control = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_INPUT_CONTROL)
        assert input_control.get_attribute("value") == element.get_attribute("text")

    def open_first_pages_and_check(self):
        first_pages = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIRST_PAGES)
        first_pages.click()
        assert first_pages.get_attribute("href").split('&')[4] in self.driver.current_url.split('&')[6]

    def next_page(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON_NEXT_PAGE).click()

    def back_page_and_check(self):
        self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON_BACK_PAGE).click()
        first_pages = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIRST_PAGES)
        assert first_pages.get_attribute("href").split('&')[4] in self.driver.current_url.split('&')[6]
