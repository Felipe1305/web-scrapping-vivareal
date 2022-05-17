from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://www.vivareal.com.br/')
select = browser.find_element_by_xpath(
    '//*[@id="js-site-main"]/section[1]/div/div/form[1]/div[1]/div/div/div[2]/select')
select.send_keys(' Mostrar Todos ', Keys.ENTER)

time.sleep(2)
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "filter-location-search-input"))
).send_keys('Teresópolis, RJ')
time.sleep(2)
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "filter-location-search-input"))
).send_keys(Keys.RETURN)

time.sleep(8)
browser.quit()
