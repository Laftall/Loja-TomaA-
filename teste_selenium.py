from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# CADASTRO

driver.get("http://127.0.0.1:5000/cadastro")

time.sleep(3)

driver.find_element(By.NAME, "email").send_keys("teste@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123456")

driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(3)

# LOGIN

driver.find_element(By.NAME, "email").send_keys("teste@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123456")

driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(4)

# ENTRA NO CATÁLOGO

driver.get("http://127.0.0.1:5000/catalogo/cerveja")

time.sleep(3)

# ADICIONA ITEM

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")

    if "/add/" in href:
        link.click()
        break

time.sleep(3)

# AUMENTA ITEM

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")

    if "/add_one/" in href:
        link.click()
        break

time.sleep(2)

# DIMINUI ITEM

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")

    if "/remove_one/" in href:
        link.click()
        break

time.sleep(2)

# VOLTA PARA HOME

driver.get("http://127.0.0.1:5000/home")

time.sleep(3)

# ENTRA NO CATÁLOGO

driver.get("http://127.0.0.1:5000/catalogo/refri")

time.sleep(3)

# ADICIONA ITEM 2

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")

    if "/add/" in href:
        link.click()
        break

time.sleep(3)

# FINALIZA COMPRA

driver.get("http://127.0.0.1:5000/finalizar")

time.sleep(3)

# VOLTAR PARA HOME

driver.get("http://127.0.0.1:5000/home")

time.sleep(3)

# LOGOUT

driver.get("http://127.0.0.1:5000/logout")

time.sleep(2)

driver.quit()