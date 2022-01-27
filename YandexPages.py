from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



class YandexSearchLocators:  # класс для хронения локаторов
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")  # локатор поисковой строки
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")  # локатор кнопки "Найти"
    LOCATOR_YANDEX_SEARCH_SUGGEST_BAR = (By.CLASS_NAME, "mini-suggest__popup-content")  # локатор таблицы с подсказками
    LOCATOR_YANDEX_SEARCH_LINKS = (By.TAG_NAME, "a")  # поиск результатов поиска
    LOCATOR_YANDEX_SEARCH_LINK_PAGES = (By.LINK_TEXT, "Картинки")


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

    def check_link_in_table_result(self, link):
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
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINK_PAGES).click()

    # def click_on_link_pages(self):
    #     return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINK_PAGES).click()

    def check_location_pages(self):
        assert "https://yandex.ru/images/?utm_source=main_stripe_big" == self.driver.current_url #пытался через current_url, почему-то проверку не проходит

        # links = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINKS)
        # links_list = []
        # for link in links:
        #     links_list.append(link.get_attribute("href"))
        #
        # assert 'yandex.ru/images/' in links_list[0]

