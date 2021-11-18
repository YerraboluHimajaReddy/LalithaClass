import unittest
from selenium import webdriver


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        driver =  webdriver.Chrome(executable_path= r'C:\\Users\\Sony\\Desktop\\Python\\Drivers\\chromedriver.exe')
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()

