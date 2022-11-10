from selenium import webdriver # the driver
from selenium.webdriver.chrome.service import Service # the chrome activities
from selenium.webdriver.support.select import Select # the select type activities
from selenium.webdriver.common.by import By # the ways to identify elemnts
from selenium.webdriver.common.keys import Keys # the
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

class OrderPaymentPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def click_next_in_OrderPayment(self):
        self.driver.find_element(By.ID,'next_btn').click()

    def safepay_username_filed(self):
        return self.driver.find_element(By.NAME,"safepay_username")

    def safepay_password_filed(self):
        return self.driver.find_element(By.NAME,"safepay_password")

    def fill_safepay_username(self, keys):
        self.safepay_username_filed().send_keys(keys)

    def fill_safepay_password(self, keys):
        self.safepay_password_filed().send_keys(keys)

    def choose_creditcard(self):
        self.driver.find_element(By.NAME,"masterCredit").click()

    def creditcard_number_filed(self):
        return self.driver.find_element(By.ID,"creditCard")

    def creditcard_CVVnumber_filed(self):
        return self.driver.find_element(By.NAME,"cvv_number")

    def creditcard_holder_name_filed(self):
        return self.driver.find_element(By.NAME,"cardholder_name")

    def click_pay_now_safepay(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#pay_now_btn_SAFEPAY")))
        element= self.driver.find_element(By.CSS_SELECTOR, "button#pay_now_btn_SAFEPAY")
        self.driver.execute_script("arguments[0].click()", element)


