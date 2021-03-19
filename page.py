from locator import *
from element import BasePageElement


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):

    def click_attendance(self):
        element = self.driver.find_element(*NavBarLocators.NAV_ATTEND_BTN)
        element.click()

    def click_regist(self):
        element = self.driver.find_element(*NavBarLocators.NAV_REGIST_BTN)
        element.click() 

    def click_admin(self):
        element = self.driver.find_element(*NavBarLocators.NAV_ADMIN_BTN)
        element.click() 

    def click_contact(self):
        element = self.driver.find_element(*NavBarLocators.NAV_CONTACT_BTN)
        element.click() 

    def click_home(self):
        element = self.driver.find_element(*NavBarLocators.NAV_HOME_BTN)
        element.click() 

class AttendancePage(BasePage):
    #course code, lecture number, image upload, sumbmit button, open camera button

    def click_submit(self):
        element = self.driver.find_element(*AttendancePageLocators.SUBMIT_BTN)
        element.click() 


class AdminLogin(BasePage):
    #usename, password, show password checkbox, login bbutton

    def check_show_pass(self):
        element = self.driver.find_element(*AdminLoginLocators.SHOW_PASS)
        element.click()  #is_enabled()

class RegisterPage(BasePage):
    #name, id, gender, email, university, faculty, courses, register, reset, uploadfile
    def click_regist_btn(self):
        element = self.driver.find_element(*RegisterPageLocators.REGIST_BTN)
        element.click()

    def click_reset_btn(self):
        element = self.driver.find_element(*RegisterPageLocators.RESET_BTN)
        element.click()

    def enter_name(self):
        element = self.driver.find_element(*RegisterPageLocators.NAME_TEXT)
        element.send_keys("Sherlock")

    def enter_id(self):
        element = self.driver.find_element(*RegisterPageLocators.ID_TEXT) 
        element.send_keys("181037")



class OpenCam(BasePage):
    def click_close_btn(self):
        element = self.driver.find_element(*OpenCamLocators.CLOSE_BTN)
        element.click()

    def click_back_btn(self):
        element = self.driver.find_element(*OpenCamLocators.CLOSE_BTN)
        element.click()
    

class ErrorPage(BasePage):  
    def click_home_btn(self):
        element = self.driver.find_element(*ErrorPageLocators.HOME_BTN)
        element.click()



