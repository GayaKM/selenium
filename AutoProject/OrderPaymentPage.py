from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class OrderPaymentPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_next_in_OrderPayment(self):
        """Method that open the section of the payment method in the order payment page"""
        self.driver.find_element(By.ID, 'next_btn').click()

    def safepay_username_filed(self):
        """Method that finds the username filed in the order payment page"""
        return self.driver.find_element(By.NAME, "safepay_username")

    def safepay_password_filed(self):
        """Method that finds the password filed in the order payment page"""
        return self.driver.find_element(By.NAME, "safepay_password")

    def fill_safepay_username(self, keys):
        """Method that fill up the username filed in the given string"""
        self.safepay_username_filed().send_keys(keys)

    def fill_safepay_password(self, keys):
        """Method that fill up the password filed in the given string"""
        self.safepay_password_filed().send_keys(keys)

    def choose_creditcard(self):
        """Method that open the master card option in the payment method in the order payment"""
        self.driver.find_element(By.NAME, "masterCredit").click()

    def creditcard_number_filed(self):
        """Method that finds the credit card filed in credit card payment method"""
        return self.driver.find_element(By.ID, "creditCard")

    def creditcard_CVVnumber_filed(self):
        """Method that finds the CVV number filed in credit card payment method"""
        return self.driver.find_element(By.NAME, "cvv_number")

    def creditcard_holder_name_filed(self):
        """Method that finds the credit card holder name filed in credit card payment method"""
        return self.driver.find_element(By.NAME, "cardholder_name")

    def click_pay_now_safepay(self):
        """Method that clicks the pay now button in the safe pay method, finsh the order, open completed order page"""
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#pay_now_btn_SAFEPAY")))
        button= self.driver.find_element(By.CSS_SELECTOR, "button#pay_now_btn_SAFEPAY")
        self.driver.execute_script("arguments[0].click()", button)