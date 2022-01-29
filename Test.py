import time

from YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.check_search_field()
    yandex_main_page.enter_word('Тензор')
    yandex_main_page.check_suggest_bar()
    yandex_main_page.click_on_the_search_button()
    yandex_main_page.check_link_in_table_result()

def test_page_in_yandex(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.check_link_pages_in_site()
    yandex_main_page.click_on_link_pages()
    yandex_main_page.check_location_pages()
    yandex_main_page.open_first_category_and_check()
    yandex_main_page.open_first_pages_and_check()
    yandex_main_page.next_page()
    yandex_main_page.back_page_and_check()


