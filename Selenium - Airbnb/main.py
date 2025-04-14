import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("window-size=400,800")

navegador = webdriver.Chrome(options=options)
navegador.get("https://www.trivago.com.br")

sleep(5)

#input_place = navegador.find_element(By.CLASS_NAME, 'dJVPMU SwVR4I')
input_place = navegador.find_element(By.CSS_SELECTOR, 'button > span > span > svg > g')
input_place.send_keys("Foz do Iguaçu")
input_place.submit()

#site = BeautifulSoup(navegador.page_source, "html.parser")
#print(site.prettify())

sleep(10)