from locator import *
#import pyautogui
from selenium.webdriver.support.ui import Select
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

    def click_open_cam(self):
        element = self.driver.find_element(*AttendancePageLocators.CAMERA_BTN)
        element.click()

    def enter_code(self, code):
        element = self.driver.find_element(*AttendancePageLocators.COURSE_CODE)
        element.send_keys(code)
    
    def enter_lec_num(self, num):
        element = self.driver.find_element(*AttendancePageLocators.LECTURE_NUM)
        element.send_keys(num)

    def upload_btn(self, mypath):
        element = self.driver.find_element(AttendancePageLocators.UPLOAD_FILE)
        element.send_keys(mypath)
        #element.click()
        #pyautogui.write(mypath) 
        #pyautogui.press('enter')

    def click_submit(self):
        element = self.driver.find_element(*AttendancePageLocators.SUBMIT_BTN)
        element.click()



class AdminLoginPage(BasePage): 
    
    def enter_username(self, name):
        element = self.driver.find_element(*AdminLoginLocators.USER_NAME)
        element.send_keys(name)

    def enter_pass(self, password):
        element = self.driver.find_element(*AdminLoginLocators.PASSWORD)
        element.send_keys(password)

    def check_show_pass(self):
        element = self.driver.find_element(*AdminLoginLocators.SHOW_PASS)
        element.click() 

    def click_login_btn(self):
        element = self.driver.find_element(*AdminLoginLocators.LOGIN_BTN)
        element.click()


class RegisterPage(BasePage):

    def click_regist_btn(self):
        element = self.driver.find_element(*RegisterPageLocators.REGIST_BTN)
        element.click()

    def click_reset_btn(self):
        element = self.driver.find_element(*RegisterPageLocators.RESET_BTN)
        element.click()
    
    def click_upload_btn(self, mypath):
        element = self.driver.find_element(*RegisterPageLocators.CHOOSE_FILE)
        element.send_keys(mypath)
        #element.click()
        #pyautogui.write(mypath) 
        #pyautogui.press('enter')

    def enter_name(self, name):
        element = self.driver.find_element(*RegisterPageLocators.NAME_TEXT)
        element.send_keys(name)

    def enter_id(self, id):
        element = self.driver.find_element(*RegisterPageLocators.ID_TEXT) 
        element.send_keys(id)

    def enter_email(self, email):
        element = self.driver.find_element(*RegisterPageLocators.EMAIL_TEXT)
        element.send_keys(email)

    def enter_courses(self, courses):
        element = self.driver.find_element(*RegisterPageLocators.COURSES_TEXT)
        element.send_keys(courses)

    def choose_uni(self, uni):
        element = Select(RegisterPageLocators.UNI_BOX)
        element.select_by_visible_text(uni)
    
    def choose_fac(self, faculty):
        element = Select(RegisterPageLocators.FAC_BOX)
        element.select_by_visible_text(faculty)

    def choose_gender(self, gender):
        element = Select(RegisterPageLocators.GENDER_BOX)
        element.select_by_visible_text(gender)
       


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



