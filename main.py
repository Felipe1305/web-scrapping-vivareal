from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Busca das cidades desejadas
#cidades = ['Teresópolis, RJ','Petrópolis - RJ', 'Nova Friburgo']
cidades = ['Teresópolis, RJ']
browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
for value in cidades:
    browser.get('https://www.vivareal.com.br/')

    select = browser.find_element_by_xpath(
        '//*[@id="js-site-main"]/section[1]/div/div/form[1]/div[1]/div/div/div[2]/select')
    select.send_keys(' Mostrar Todos ', Keys.ENTER)

    time.sleep(2)
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "filter-location-search-input"))
    ).send_keys(value)
    time.sleep(2)
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "filter-location-search-input"))
    ).send_keys(Keys.RETURN)

# Extraindo todos os links de imóveis da cidade


# Encontrando o conteiner com os anúncios
elem = browser.find_element_by_xpath(
    '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[1]')
elements = elem.find_elements_by_tag_name('article')

# Para cada card retirar o link do anúncio
for ele in elements:
    print(ele.find_element_by_tag_name('a').get_attribute('href'))


time.sleep(8)
browser.quit()
