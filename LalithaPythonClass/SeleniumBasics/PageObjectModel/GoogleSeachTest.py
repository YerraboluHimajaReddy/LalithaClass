import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleSearchTest(unittest.TestCase):


    def test_GoogleSearch(self):
        driver= webdriver.Chrome("C:\\Users\\Sony\\Desktop\\Python\\Drivers\\chromedriver.exe")
        self.driver=driver
        time.sleep(2)
        driver.maximize_window()  # to maximize the window
        driver.get("http://www.google.com")  # to launch a web browser
        time.sleep(2)

        # Perform search operation
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Lambdatest")
        elem.submit()

    def tearDown(self):
        # Close the browser.
        self.driver.close()
        #self.driver.quit()


if __name__ == '__main__':
    unittest.main()
