import unittest
import page
from selenium import webdriver


class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.implicitly_wait(50)


    def test_register(self): #new student
        mypage1 = page.HomePage(self.driver)
        mypage1.click_regist()
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
        mypage1 = page.HomePage(self.driver)
        mypage1.click_attendance()
        mypage = page.AttendancePage(self.driver)
        mypage.enter_lec_num("3") #edit this
        mypage.enter_code("CS321") #edit this
        mypage.upload_btn("Bill_Gates.jpg") #edit this
        self.driver.implicitly_wait(1000)
        mypage.click_submit()


    def test_admin(self):  # right admin
        mypage1 = page.HomePage(self.driver)
        mypage1.click_admin()
        mypage = page.AdminLoginPage(self.driver)
        mypage.enter_username("Mosa99") 
        mypage.enter_pass("123456789") 
        mypage.check_show_pass()
        mypage.click_login_btn()
        #assert redirecting 

    def test_error(self):
        self.driver.get("file:///C:/Users/Menna%20Shazly/Desktop/New%20folder/app/templates/error.html")
        self.driver.implicitly_wait(50)
        mypage1 = page.ErrorPage(self.driver)
        mypage1.click_home_btn()
        assert "127.0.0.1:5000" in self.driver.title
        
    def test_cam(self):
        self.driver.get("http://127.0.0.1:5000/attendance")
        self.driver.implicitly_wait(50)
        mypage = page.OpenCam(self.driver)
        mypage.click_back_btn()
        assert "127.0.0.1:5000" in self.driver.title


    def test_contact(self):
        mypage1 = page.HomePage(self.driver)
        mypage1.click_contact()
        assert "contact" in self.driver.title
       

    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()
