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
        mypage.enter_username("mosa") #edit this
        mypage.enter_pass("mosa123456789")  #edit this
        mypage.check_show_pass()
        mypage.click_login_btn()
        #assert redirecting 


    def test_contact(self):
        mypage1 = page.HomePage(self.driver)
        mypage1.click_contact()
        assert "contact" in self.driver.title
       

    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()
