from selenium.webdriver.common.by import By


class NavBarLocators(object):
    #A class for all Navigation bar locators.

    NAV_HOME_BTN = (By.XPATH, "/html/body/div[1]/a[1]" )
    NAV_ATTEND_BTN = (By.XPATH, "/html/body/div[1]/a[2]")
    NAV_REGIST_BTN = (By.XPATH, "/html/body/div[1]/a[3]")
    NAV_ADMIN_BTN = (By.XPATH, "/html/body/div[1]/a[4]" )
    NAV_CONTACT_BTN = (By.XPATH, "/html/body/div[1]/a[5]")


class AttendancePageLocators(object):
    #A class for all index page locators.

    COURSE_CODE = (By.ID, "course_code")
    LECTURE_NUM = (By.ID, "lecture_number")
    UPLOAD_FILE = (By.ID, "uploaded_file")
    SUBMIT_BTN = (By.ID, "submit_attend")
    CAMERA_BTN = (By.ID, "opencamera")


class AdminLoginLocators(object):
    #A class for all Admin page locators.
    
    USER_NAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SHOW_PASS = (By.ID, "showpassword")
    LOGIN_BTN = (By.ID, "login")


class RegisterPageLocators(object):
    #A class for all register page locators.

    NAME_TEXT = (By.ID, "fullname")
    ID_TEXT = (By.ID, "studentid")
    GENDER_BOX = (By.ID, "gender")
    EMAIL_TEXT = (By.ID, "email")
    UNI_BOX = (By.ID, "university")
    FAC_BOX = (By.ID, "faculty")
    COURSES_TEXT = (By.ID, "courses")
    REGIST_BTN = (By.ID, "register")
    RESET_BTN = (By.ID, "reset")
    CHOOSE_FILE = (By.ID, "uploadImg")
   

class OpenCamLocators(object):
    #A class for all camera page locators.

   BACK_BTN = (By.XPATH, "/html/body/div[2]/h2[2]/a")


class ErrorPageLocators(object):
    #A class for all Error page locators.

    HOME_BTN = (By.ID, "homePage")
