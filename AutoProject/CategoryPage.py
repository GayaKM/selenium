from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *
from ProductPage import ProductPage


class CategoryPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.product = ProductPage(self.driver)

    def find_all_products_in_category(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".categoryRight>ul>li")

    def click_product(self):
        list_p = self.find_all_products_in_category()
        rand = randint(0, len(list_p)-1)
        list_p[rand].click()
        while self.product.product_name() == "BOSE SOUNDLINK AROUND-EAR WIRELESS HEADPHONES II":
            self.driver.back()
            rand = randint(0, len(list_p) - 1)
            list_p[rand].click()

    def category_headline(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-ng-class='{ noPromotedProduct : viewAll }']").text

