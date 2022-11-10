from selenium import webdriver # the driver
from selenium.webdriver.chrome.service import Service # the chrome activities
from selenium.webdriver.support.select import Select # the select type activities
from selenium.webdriver.common.by import By # the ways to identify elemnts
from selenium.webdriver.common.keys import Keys # the
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

class GeneralPage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def find_cart(self):
        return self.driver.find_element(By.ID, "menuCart")

    def click_cart(self):
        self.find_cart().click()

    def find_the_int_number(self, word:str):
        num=0
        for i in word:
            if i.isnumeric():
                num *= 10
                num += int(i)
        return num

    def product_quantities_cart_window(self):
        products_quas = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td[2]/a/label[1]")
        for i in range(len(products_quas)):
            text = products_quas[i].text
            products_quas[i]=self.find_the_int_number(text)
        return products_quas

    def product_prices_cart_window(self):
        product_prices = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/p")
        prices=[]
        for i in range(len(product_prices)):
            text_p = product_prices[i].text
            loction = text_p.find("$")
            text_p = text_p[loction+1:]
            loction = text_p.find(",")
            if loction>0:
                text_p=text_p[:loction]+text_p[loction+1:]
            prices.append(float(text_p))
        return prices

    def total_quantity_cart_window(self):
        total_quantity = self.driver.find_element(By.CSS_SELECTOR,"label[class='roboto-regular ng-binding']")
        return self.find_the_int_number(total_quantity.text)

    def product_color_in_window(self):
        list_colors=self.driver.find_elements (By.CSS_SELECTOR,'span[class="ng-binding"]')
        names=[]
        for i in range(len(list_colors)):
            names.append(list_colors[i].text)
        return names


    def products_in_cart_window(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"[class='removeProduct iconCss iconX']")

    def remove_product_from_cart_window(self):
        product_list = self.products_in_cart()
        product_list[randint(0,len(product_list)-1)].click()

    def click_the_logo(self):
        self.driver.find_element(By.CLASS_NAME,'logo').click()

    def find_loction_navigationline(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[class='select  ng-binding']").text

    def products_names_in_window(self):
        list_names = self.driver.find_elements(By.XPATH, '//a/h3')
        for i in range(len(list_names)):
            list_names[i] = list_names[i].text
        return list_names

    def click_register_in_checkout(self):
        self.driver.find_element(By.ID,"registration_btnundefined").click()

    def click_user_logo(self):
        logo = self.driver.find_element(By.ID, "menuUser").click

    def click_my_account(self):
        self.click_user_logo()
        self.driver.find_element(By.CSS_SELECTOR, "[translate='My_account']").click()

    def click_my_orders(self):
        self.click_user_logo()
        self.driver.find_element(By.LINK_TEXT, "My orders").click()

    def order_mesage(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")

    def click_delete_account(self):
        self.driver.find_element(By.CLASS_NAME, "deleteBtnText").click()

    def find_order_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="left ng-binding"]').text

