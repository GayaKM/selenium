from selenium import webdriver # the driver
from selenium.webdriver.chrome.service import Service # the chrome activities
from selenium.webdriver.support.select import Select # the select type activities
from selenium.webdriver.common.by import By # the ways to identify elemnts
from selenium.webdriver.common.keys import Keys # the
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *

class CategoryPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def find_all_products_in_category(self):
       return self.driver.find_elements(By.CSS_SELECTOR,".categoryRight>ul>li")

    def click_product(self):
        list = self.find_all_products_in_category()
        list[randint(0,len(list)-1)].click()

    def category_headline(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[data-ng-class='{ noPromotedProduct : viewAll }']").text

