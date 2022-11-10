from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class CreateAccountPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def username_filed(self):
        """Method that finds the username filed in the create account page"""
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def email_filed(self):
        """Method that finds the email filed in the create account page"""
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def password_filed(self):
        """Method that finds the password filed in the create account page"""
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_filed(self):
        """Method that finds the confirmation password filed in the create account page"""
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def fill_username(self, keys):
        """Method that fills up the username filed with the given string"""
        self.username_filed().send_keys(keys)

    def fill_email(self, keys):
        """Method that fills up the email filed with the given string"""
        self.email_filed().send_keys(keys)

    def fill_passwords(self, keys):
        """Method that fills up the password and confirm password filed with the given string"""
        self.password_filed().send_keys(keys)
        self.confirm_password_filed().send_keys(keys)

    def register(self):
        """Method that finish the register process by clicking the i agree checkbox and the register button"""
        self.driver.find_element(By.NAME, "i_agree").click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[a-value="REGISTER"]'))).click()