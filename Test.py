from YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.check_search_field()
    yandex_main_page.enter_word('Тензор')
    yandex_main_page.check_suggest_bar()
    yandex_main_page.click_on_the_search_button()
    yandex_main_page.check_link_in_table_result('tensor.ru')

def test_page_in_yandex(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.check_link_pages_in_site()
    yandex_main_page.check_location_pages()



