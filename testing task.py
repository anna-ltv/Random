import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/")

    element = browser.find_element_by_css_selector("input.gLFyf.gsfi")
    element.send_keys("новости")
    #time.sleep(3)

    button = browser.find_element_by_css_selector("input.gNO89b")
    button.click()
    #time.sleep(3)

    random_news = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3/span')
    random_news.click()
    #time.sleep(3)

    my_search_list = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[contains(@class, 'cell-list__item-title')]")))
    myRandomNumber = random.randint(0, len(my_search_list))
    random_header = my_search_list[myRandomNumber].text
    print(random_header)

finally:
    browser.quit()

# try:
#     browser = webdriver.Chrome()
#     browser.get("https://www.google.com/")
#
#     element_1 = browser.find_element_by_name("q")
#     element_1.send_keys("новости")
#     element_1.send_keys(Keys.ENTER)
#
#     some_news_1 = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3/span')
#     some_news_1.click()
#
# finally:
#     browser.quit()

