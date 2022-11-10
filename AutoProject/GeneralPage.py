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
        self.wait = WebDriverWait(driver, 10)

    def find_cart(self):
        """Method that finds the cart icon element"""
        return self.driver.find_element(By.ID, "menuCart")

    def click_cart(self):
        """Method that enters the cart page"""
        self.find_cart().click()

    def find_the_int_number(self, word):
        """Method that changes given string to integer type number and returns it"""
        num = 0
        for i in word:
            if i.isnumeric():
                num *= 10
                num += int(i)
        return num

    def product_quantities_cart_window(self):
        """Method that returns a list of the quantities of the products from the cart window"""
        products_quas = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")
        for i in range(len(products_quas)):
            text = products_quas[i].text
            products_quas[i] = self.find_the_int_number(text)
        return products_quas

    def product_prices_cart_window(self):
        """Method that returns a list of the prices of the products from the cart window"""
        product_prices = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]/p")
        prices = []
        for i in range(len(product_prices)):
            text_p = product_prices[i].text
            location = text_p.find("$")
            text_p = text_p[location+1:]
            location = text_p.find(",")
            if location > 0:
                text_p = text_p[:location]+text_p[location+1:]
            prices.append(float(text_p))
        return prices

    def total_quantity_cart_window(self):
        """Method that returns the sum up of the quantity of the products from the cart window"""
        total_quantity = self.driver.find_element(By.CSS_SELECTOR, "label[class='roboto-regular ng-binding']")
        return self.find_the_int_number(total_quantity.text)

    def product_color_in_window(self):
        """Method that returns a list of the colors of the products from the cart window"""
        list_colors = self.driver.find_elements(By.CSS_SELECTOR, 'span[class="ng-binding"]')
        names = []
        for i in range(len(list_colors)):
            names.append(list_colors[i].text)
        return names

    def products_in_cart_window(self):
        """Method that finds all the products elements from the cart window by their removing option"""
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='removeProduct iconCss iconX']")

    def remove_product_from_cart_window(self):
        """Method that removes a random product from the cart window"""
        product_list = self.products_in_cart_window()
        product_list[randint(0, len(product_list)-1)].click()

    def click_the_logo(self):
        """Method the returns to the home page by clicking the logo"""
        self.driver.find_element(By.CLASS_NAME, 'logo').click()

    def find_location_navigationline(self):
        """Method that returns the text that shows your location in the site from the navigation line """
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

    def products_names_in_window(self):
        """Method that returns a list of the names of the products from the cart window"""
        list_names = self.driver.find_elements(By.XPATH, '//a/h3')
        for i in range(len(list_names)):
            list_names[i] = list_names[i].text
        return list_names

    def click_register_in_checkout(self):
        """Method that clicks the register button in the beginning of the check-out process"""
        self.driver.find_element(By.ID, "registration_btnundefined").click()

    def click_user_logo(self):
        """Method that clicks the account icon and opens the sign in or the account menu"""
        self.driver.find_element(By.ID, "menuUser").click()

    def click_my_account(self):
        """Method that opens my account page"""
        self.click_user_logo()
        self.driver.find_element(By.CSS_SELECTOR, "[translate='My_account']").click()

    def click_my_orders(self):
        """Method that opens my orders page"""
        self.click_user_logo()
        self.driver.find_element(By.LINK_TEXT, "My orders").click()

    def order_message(self):
        """Method that finds the message that says the order completed in the order completed page"""
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")

    def click_delete_account(self):
        """Method that deletes a sign in account"""
        self.driver.find_element(By.CLASS_NAME, "deleteBtnText").click()

    def find_order_number(self):
        """Method that returns the latest (most recant) order that completed from the sign in account"""
        order_numbers = self.driver.find_elements(By.CSS_SELECTOR, '[class="left ng-binding"]')
        return order_numbers[0].text