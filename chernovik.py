from pprint import pprint

from selenium import webdriver

driver = webdriver.Chrome()

tensor = driver.get("https://yandex.ru/images/?utm_source=main_stripe_big")

print(driver.current_url)


# driver.quit()