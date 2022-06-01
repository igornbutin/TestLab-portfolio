# что делает: заходит на ya.ru, посыласет запрос "pavarotti sting", дожидается и закрывает браузер
# как улучшить: заменить xpath на более надежные id
# python 3.10.4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\webdriver\chromedriver')

# запрос GET
driver.get('https://ya.ru/')

# выделяет элемент
searchBox = driver.find_element_by_xpath('//*[@id="text"]')

# посылает текст якобы с клавиатуры
searchBox.send_keys('pavarotti sting')

# декларирует и нажимает кнопку "Найти"
serchButton = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/div[2]/button').click()

# дожидается и выходит из браузера
try:
    element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'service service_name_images i-bem'))
    )
finally:
    driver.quit()
