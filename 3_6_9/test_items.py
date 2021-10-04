import time
import math
link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_link_different_languages(browser):
    browser.get(link)
    time.sleep(7)
    assert browser.find_element_by_css_selector(".btn-primary").text != None  