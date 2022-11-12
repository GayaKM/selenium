from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *
from GeneralPage import GeneralPage


class CartPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.general = GeneralPage(self.driver)

    def total_price(self):
        """Method that returns the total price of the products in the cart in float type"""
        price = self.driver.find_element(By.XPATH, "//tfoot/tr/td[2]/span[2]").text
        i = price.find("$")
        price = price[i + 1:]
        i = price.find(",")
        if i > 0:
            price = price[:i] + price[i + 1:]
        return float(price)

    def products_names(self):
        """Method that returns a list of the names of the products in the cart"""
        list_names = self.driver.find_elements(By.XPATH, '//article/div/table/tbody/tr/td[2]/label')
        for i in range(len(list_names)):
            list_names[i] = list_names[i].text
        return list_names

    def products_quantities(self):
        """Method that returns a list of the quantities of the products in the cart"""
        list_q = self.driver.find_elements(By.XPATH, '//ul/li/tool-tip-cart/div/table/tbody/tr/td[2]/a/label[1]')
        for i in range(len(list_q)):
            list_q[i] = self.general.find_the_int_number(list_q[i].text)
        return list_q

    def products_price(self):
        """Method that returns a list of the prices of the products in the cart"""
        prices = self.driver.find_elements(By.XPATH, "//ul/li/tool-tip-cart/div/table/tbody/tr/td[3]/p")
        for i in range(len(prices)):
            prices[i] = prices[i].text
            j = prices[i].find("$")
            prices[i] = prices[i][j + 1:]
            j = prices[i].find(",")
            if j > 0:
                prices[i] = prices[i][:j] + prices[i][j + 1:]
            prices[i] = float(prices[i])
        return prices

    def products_colors(self):
        """Method that returns a list of the color elements of the products in the cart"""
        return self.driver.find_element(By.XPATH, '//article/div/table/tbody/tr/td[4]/span')

    def click_checkout(self):
        """Method that starts the check-out presses clicks the check-out button and open the order payment page"""
        self.driver.find_element(By.ID, "checkOutButton").click()

    def empty_cart_message(self):
        """Method that finds the order complete message in the order completed page"""
        list_message = self.driver.find_elements(By.CSS_SELECTOR, 'label[translate="Your_shopping_cart_is_empty"][class="center roboto-medium ng-scope"]')
        return list_message[1]

    def zero_items_in_cart(self):
        """Method that finds the  message that shows 0 items in an empty cart page"""
        number = self.driver.find_element(By.XPATH, "//div/tool-tip-cart/div/div/label/span").text
        number = self.general.find_the_int_number(number)
        return number

    def edit_product(self, num):
        """Method that get the index of the spesific """
        return self.driver.find_elements(By.LINK_TEXT, "EDIT")[num]

    def click_edit(self,num):
        self.edit_product(num).click()