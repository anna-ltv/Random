"""Задание № 2
С помощью инструмента автоматизации тестирования Selenium, а также chromedriver или geckodriver(в случае использования браузера FireFox)  используя язык программирования Python разработать программу, которая выполняет следующие действия:
•	Открывает браузер (chrome, firefox);
•	Осуществляет переход на google.com;
•	В поисковой строке вводит слово "новости", после чего выполняется поиск по заданному слову;
•	На открывшейся странице выполняется переход на раздел "новости";
•	Вывести в терминале заголовок случайной новости в пределах первой страницы.
"""
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/")

    element = browser.find_element_by_css_selector("input.gLFyf.gsfi")
    element.send_keys("новости")

    button = browser.find_element_by_css_selector("input.gNO89b")
    button.click()

    some_news = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3/span')
    some_news.click()

    my_search_list = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[contains(@class, 'cell-list__item-title')]")))
    myRandomNumber = random.randint(0, len(my_search_list))
    random_header = my_search_list[myRandomNumber].text
    print(random_header)

finally:
    browser.quit()
    

