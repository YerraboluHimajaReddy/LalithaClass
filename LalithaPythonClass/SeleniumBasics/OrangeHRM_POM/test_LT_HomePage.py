import unittest

from LalithaPythonClass.SeleniumBasics.OrangeHRM_POM.LocatorHandlings__LoginPage import LocatorHandlings__LoginPage
from LalithaPythonClass.SeleniumBasics.PageObjectModel.Tests.WebDriverSetup import WebDriverSetup
import time


class test_LT_HomePage(WebDriverSetup,unittest.TestCase):

    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(5)
        self.driver.set_page_load_timeout(30)
        web_page_title = "OrangeHRM"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

    def test_Pagecredentials(self):
         LocatorHandlings__LoginPage.lt_login_user_name.send_keys("Admin")


if __name__ == '__main__':
    unittest.main()
