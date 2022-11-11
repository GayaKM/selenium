from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *


class HomePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_category(self):
        """Method that enters a random category that comes from the random_category_id"""
        category = self.driver.find_element(By.ID, self.random_category_id())
        category.click()

    def random_category_id(self):
        """Method that return a random category id from the category id list it declares"""
        category_ids = ["speakersTxt", "tabletsTxt", "laptopsTxt", "miceTxt", "headphonesTxt"]
        return category_ids[randint(0, len(category_ids)-1)]

    def username(self):
        """Method that finds the username in the sign in window"""
        return self.driver.find_element(By.NAME, "username")

    def password(self):
        """Method that finds the password in the sign in window"""
        return self.driver.find_element(By.NAME, "password")

    def click_user_signout(self):
        """Method that sign-out the signed in account"""
        self.driver.find_element(By.CSS_SELECTOR, '[ng-click="signOut($event)"]').click()

    def fill_password(self, keys):
        """Method that fills the password in the sign in window"""
        self.password().send_keys(keys)

    def click_signin(self):
        """click the signin button in the signin window"""
        self.driver.find_element(By.ID, "sign_in_btnundefined").click()

    def fill_username(self,name):
        """Method that fills the username in the sign in window"""
        self.username().send_keys(name)