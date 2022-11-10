from selenium import webdriver # the driver
from selenium.webdriver.chrome.service import Service # the chrome activities
from selenium.webdriver.support.select import Select # the select type activities
from selenium.webdriver.common.by import By # the ways to identify elemnts
from selenium.webdriver.common.keys import Keys # the
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

class CreateAccountPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def username_filed(self):
        return self.driver.find_element(By.NAME,"usernameRegisterPage")

    def email_filed(self):
        return self.driver.find_element(By.NAME,"emailRegisterPage")

    def password_filed(self):
        return self.driver.find_element(By.NAME,"passwordRegisterPage")

    def confirm_password_filed(self):
        return self.driver.find_element(By.NAME,"confirm_passwordRegisterPage")

    def fill_username(self, keys):
        self.username_filed().send_keys(keys)

    def fill_email(self, keys):
        self.email_filed().send_keys(keys)

    def fill_passwords(self, keys):
        self.password_filed().send_keys(keys)
        self.confirm_password_filed().send_keys(keys)

    def register(self):
        self.driver.find_element(By.NAME, "i_agree").click()
        self.driver.find_element(By.CSS_SELECTOR, '[a-value="REGISTER"]').click()


