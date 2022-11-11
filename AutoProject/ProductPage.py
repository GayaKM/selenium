from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from time import sleep


class ProductPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_quantity(self, num_of_times):
        for i in range(num_of_times):
            self.driver.find_element(By.CLASS_NAME, "plus").click()

    def subtract_quantity(self, num_of_times):
        for i in range(num_of_times):
            self.driver.find_element(By.CLASS_NAME, "minus disableBtn").click()

    def product_name(self):
        return self.driver.find_element(By.XPATH, "//section/article/div[2]/div[2]/h1").text

    def product_price(self):
        price = self.driver.find_element(By.XPATH, "//section/article/div[2]/div[2]/h2").text
        i = price.find("$")
        price = price[i+1:]
        i = price.find(",")
        if i > 0:
            price = price[:i]+price[i+1:]
        i = 0
        while i <= len(price)-1 and (price[i].isnumeric() or price[i] == '.'):
            i += 1
        price = price[:i]
        return float(price)

    def add_to_cart(self):
        self.driver.find_element(By.NAME, "save_to_cart").click()

    def product_colors_id(self):
        return self.driver.find_elements(By.ID, "rabbit")

    def product_colors_title(self):
        list_colors = self.product_colors_id()
        for i in range(len(list_colors)):
            list_colors[i] = list_colors[i].get_attribute('title')
        return list_colors

    def select_color(self):
        colors_id = self.product_colors_id()
        rand = randint(0, len(colors_id)-1)
        colors_id[rand].click()
        list_colors = self.product_colors_title()
        return list_colors[rand]