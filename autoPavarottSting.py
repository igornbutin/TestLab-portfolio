# что делает: заходит на ya.ru и посыласет запрос на выдачу по запросу "pavarotti sting"
# как улучшить: заменить xpath на id

from selenium import webdriver
driver = webdriver.Chrome('C:\webdriver\chromedriver')

# запрос GET
driver.get('https://ya.ru/')

# выделяю элемент
searchBox = driver.find_element_by_xpath('//*[@id="text"]')

# посылаю текст якобы с клавиатуры
searchBox.send_keys('pavarotti sting')

# декларирую и нажимаю кнопку "Найти"
serchButton = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/div[2]/button').click()

# выход из браузера
driver.quit()