from selenium import webdriver  #get access to webdriver
from selenium.webdriver.common.keys import Keys  #get access to keyboard inputs
import time #to know time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://127.0.0.1:5000/")

code = driver.find_elements_by_id("course_code")
code.send_keys("CS231")
lec_num = driver.find_elements_by_id("lecture_number")
lec_num.send_keys("3")

#clear() used to clear text box before typing
#driver.implicitly_wait(10)

time.sleep(15)
driver.quit() 