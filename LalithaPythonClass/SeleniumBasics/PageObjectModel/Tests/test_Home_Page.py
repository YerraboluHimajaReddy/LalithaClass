import unittest

from LalithaPythonClass.SeleniumBasics.PageObjectModel.Tests.HomePage import HomePage
from LalithaPythonClass.SeleniumBasics.PageObjectModel.Tests.WebDriverSetup import WebDriverSetup


class Google_HomePage(WebDriverSetup):
    def test_Home_Page(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)
        actual_web_page_title = "Goole"
        expected_web_page_title=driver.title

        try:
            print(" driver.title :", expected_web_page_title)
            print(" web_page_title :" , actual_web_page_title)
            if expected_web_page_title == actual_web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(expected_web_page_title, actual_web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        # Create an instance of the class so that you we can make use of the methods
        # in the class
#home_page = HomePage(driver)


if __name__ == '__main__':
    unittest.main()

