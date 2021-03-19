import unittest
import page
from selenium import webdriver


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()


def test_register(self):
        self.driver.get("http://127.0.0.1:5000/register")
        self.driver.implicitly_wait(50)
        mypage = page.RegisterPage(self.driver)
        mypage.enter_name("Menna Shazly")
        mypage.enter_id("181037")
        mypage.enter_email("mennam322@gmail.com")
        mypage.enter_courses("CS182,IT231,MT222,CS021,SE000")
        mypage.choose_uni("Suez")
        mypage.choose_fac("FCI")
        mypage.choose_gender("Female")
        mypage.click_upload_btn("Menna.png")
        mypage.click_regist_btn()


    def test_attendance(self):
        self.driver.get("http://127.0.0.1:5000/attendance")
        self.driver.implicitly_wait(50)
        mypage = page.AttendancePage(self.driver)
        mypage.enter_lec_num("3")
        mypage.enter_code("CS321")
        #mypage.upload_btn("Testing\Bill_Gates.jpg")
        #self.driver.implicitly_wait(1000)
        #mypage.click_submit()

    def test_admin(self):
        self.driver.get("http://127.0.0.1:5000/admin/login")
        self.driver.implicitly_wait(50)
        mypage = page.AdminLoginPage(self.driver)
        mypage.enter_username("Sherlock")
        mypage.enter_pass("sherlock221B221B")
        mypage.check_show_pass()
        mypage.click_login_btn()  

    def test_nav(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.implicitly_wait(50)
        mypage = page.HomePage(self.driver)
        #mypage.click_regist()
        mypage.click_attendance()
        mypage.click_contact()
        mypage.click_admin()
        mypage.click_home()

    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()
