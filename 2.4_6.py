from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc_1(x):
 return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
#browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
 


y = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100") )
print("kk"+str(y)+"1")
browser.find_element_by_id('book').click()

x=browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(calc_1(x))
browser.find_element_by_id('solve').click()


time.sleep(20)
browser.quit()