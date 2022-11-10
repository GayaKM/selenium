from selenium import webdriver # the driver
from selenium.webdriver.chrome.service import Service # the chrome activities
from selenium.webdriver.support.select import Select # the select type activities
from selenium.webdriver.common.by import By # the ways to identify elemnts
from selenium.webdriver.common.keys import Keys # the
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *
from GeneralPage import GeneralPage

class CartPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)
        self.general = GeneralPage(self.driver)

    def total_price(self):
        price=self.driver.find_element(By.XPATH, "//tfoot/tr/td[2]/span[2]").text
        i = price.find("$")
        price = price[i + 1:]
        i = price.find(",")
        if i > 0:
            price = price[:i] + price[i + 1:]
        return float(price)

    def products_names(self):
        list_names=self.driver.find_elements(By.XPATH, '//article/div/table/tbody/tr/td[2]/label')
        for i in range(len(list_names)):
            list_names[i]=list_names[i].text
        return list_names

    def products_quantities(self):
        list = self.driver.find_elements(By.XPATH, '//ul/li/tool-tip-cart/div/table/tbody/tr/td[2]/a/label[1]')
        for i in range(len(list)):
            list[i]= self.general.find_the_int_number(list[i].text)
        return list

    def products_price(self):
        prices = self.driver.find_elements(By.XPATH, "//ul/li/tool-tip-cart/div/table/tbody/tr/td[3]/p")
        for j in range(len(prices)):
            prices[j]=prices[j].text
            i = prices[j].find("$")
            prices[j] = prices[j][i + 1:]
            i = prices[j].find(",")
            if i > 0:
                prices[j] = prices[j][:i] + prices[j][i + 1:]
            prices[j]=float(prices[j])
        return prices

    def products_colors(self):
        return self.driver.find_element(By.XPATH,'//article/div/table/tbody/tr/td[4]/span')

    def click_checkout(self):
        self.driver.find_element(By.ID,"checkOutButton").click()

    def empty_cart_masege(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="Your_shopping_cart_is_empty"]')

    def zero_items_in_cart(self):
        number = self.driver.find_element(By.XPATH,"//div/tool-tip-cart/div/div/label/span").text
        number = self.general.find_the_int_number(number)
        return number

