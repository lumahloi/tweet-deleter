from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
from selenium.webdriver.common.keys import Keys

# Configura o Selenium WebDriver para Firefox
driver = webdriver.Firefox()

driver.get('https://x.com/i/flow/login')

input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]'))
)
input_element.send_keys("@user")

next_button = driver.find_element(By.CSS_SELECTOR, 'button[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]')
next_button.click()

pass_element = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]'))
)
pass_element.send_keys("password")

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]')
submit_button.click()

# Espera a página carregar
time.sleep(5)

# Abre a página desejada após a autenticação
driver.get('https://x.com/search?q=from%3A%40lumalter_%20until%3A2020-12-30&src=typed_query&f=top')

# Espera a página carregar
time.sleep(5)

# Loop para continuar enquanto o elemento 'elemento_jota' estiver presente
while True:
    try: 
        btn3 = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="caret"]'))
        )
        btn3.click()

        deletebtn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="css-175oi2r r-1777fci r-faml9v"]'))
        )
        deletebtn.click()

        confirmbtn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="confirmationSheetConfirm"]'))
        )
        confirmbtn.click()
    except Exception as e:
        print(f'Erro: {e}')
        break

# Fecha o navegador
driver.quit()
