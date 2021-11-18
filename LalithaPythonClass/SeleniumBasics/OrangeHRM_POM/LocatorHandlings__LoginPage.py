from selenium.webdriver.common.by import By
from selenium import webdriver

class LocatorHandlings__LoginPage(object):

    def credentials(self, driver):
        self.driver = driver
        self.lt_login_user_name = driver.find_element(By.XPATH, OHRM_LoginPage_Locators.username)
        self.lt_login_password = driver.find_element(By.XPATH, OHRM_LoginPage_Locators.password)
        self.lt_login_button = driver.find_element(By.XPATH, OHRM_LoginPage_Locators.login_button)
        self.lt_ForgotPassword = driver.find_element(By.XPATH, OHRM_LoginPage_Locators.forgotPassword_Link)

    def get_username(self):
        return self.lt_login_user_name

    def Enter_username(self,username):
         self.lt_login_user_name.send_keys(username)

    def get_password(self):
        return self.lt_login_password

    def get_login_button(self):
        return self.lt_login_button

    def get_login_button(self):
        return self.lt_ForgotPassword
