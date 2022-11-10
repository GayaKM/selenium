from selenium import webdriver # the driver
from selenium.webdriver.chrome.service import Service # the chrome activities
from selenium.webdriver.support.select import Select # the select type activities
from selenium.webdriver.common.by import By # the ways to identify elemnts
from selenium.webdriver.common.keys import Keys # the
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *

class HomePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def enter_catagory(self):
        category = self.driver.find_element(By.ID, self.random_category_id())
        category.click()

    def random_category_id(self):
        category_ids = ["speakersTxt", "tabletsTxt", "laptopsTxt", "miceTxt", "headphonesTxt"]
        return category_ids[randint(0,len(category_ids)-1)]



