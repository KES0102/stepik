from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

#Функция принимает Х, считает по формуле и возвращает значение тип str ---
def calc_1(x):                                                        #---
 return str(math.log(abs(12*math.sin(int(x)))))                       #---
#-------------------------------------------------------------------------

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

#Нахожу объект с ценой, жду снижения цены до 100$ и кликаю кнопку book-----
y = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element  #---
((By.ID, "price"), "$100") )                                           #---
browser.find_element_by_id('book').click()                             #---
#--------------------------------------------------------------------------

#Нахожу значение Х, подставляю в формулу,----------------------------------
#Результат отправляю в поле input, жму на кнопку Submit                #---
x=browser.find_element_by_id('input_value').text                       #---
browser.find_element_by_id('answer').send_keys(calc_1(x))              #---
browser.find_element_by_id('solve').click()                            #---
#--------------------------------------------------------------------------

#Жду 20 с, чтобы скопировать код и выход-----------------------------------
time.sleep(20)                                                         #---
browser.quit()                                                         #---
#--------------------------------------------------------------------------