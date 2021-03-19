import unittest
import page
from selenium import webdriver


class FaceRecognetion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.implicitly_wait(50)

    def test_nav(self):
        home_page = page.HomePage(self.driver)
        assert home_page.click_attendance()
        
        
    #def test_errorpage(self):

    #   error_page = page.ErrorPage(self.driver)
    #    assert error_page.click_home_btn()

    #test_nav(self):
    #    home_page = page.HomePage(self.driver)
    #    assert

    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()
