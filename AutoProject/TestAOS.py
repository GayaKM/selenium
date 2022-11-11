from unittest import TestCase
from ProductPage import ProductPage
from HomePage import HomePage
from GeneralPage import GeneralPage
from CategoryPage import CategoryPage
from CartPage import CartPage
from CreateAccountPage import CreateAccountPage
from OrderPaymentPage import OrderPaymentPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class TestAOS(TestCase):

    def setUp(self):
        service_chrome = Service(r"C:\Users\user\Desktop\Celenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.homepage = HomePage(self.driver)
        self.general = GeneralPage(self.driver)
        self.product = ProductPage(self.driver)
        self.category = CategoryPage(self.driver)
        self.cart = CartPage(self.driver)
        self.create_account = CreateAccountPage(self.driver)
        self.payment = OrderPaymentPage(self.driver)

    def test_1_right_quantity(self):
        """Test that the sum of the quantity of the products in the cart and while their added are the same"""
        num_products_in_test = 0
        for i in range(2):
            self.homepage.enter_category()
            self.category.click_product()
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            num_products_in_test += rand + 1
            self.product.add_to_cart()
            self.general.click_the_logo()
        self.assertEqual(sum(self.general.product_quantities_cart_window()), self.general.total_quantity_cart_window())
        self.assertEqual(num_products_in_test, self.general.total_quantity_cart_window())

    def test_2_cart_window_in_sync(self):
        """Test that the products details from the cart window are identical to the ones in the products pages"""
        products_names = []
        products_quantities = []
        products_color = []
        products_price = []
        for i in range(3):
            self.homepage.enter_category()
            self.category.click_product()
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            color = self.product.select_color()
            products_names.append(self.product.product_name())
            products_quantities.append(rand+1)
            products_color.append(color)
            products_price.append(self.product.product_price())
            self.product.add_to_cart()
            self.general.click_the_logo()
        window_products_names = self.general.products_names_in_window()
        window_products_quantities = self.general.product_quantities_cart_window()
        window_products_colors = self.general.product_color_in_window()
        window_products_prices = self.general.product_prices_cart_window()
        for i in range(3):
            self.assertEqual(window_products_names[i][:27], products_names[-1-i][:27])
            self.assertEqual(window_products_quantities[i], products_quantities[-1-i])
            self.assertEqual(window_products_colors[i], products_color[-1-i])
            print(window_products_prices, products_price)
            self.assertEqual(window_products_prices[i], products_price[-1-i]*products_quantities[-1-i])

    def test_3_product_removed_from_cart_window(self):
        """Test that after removing product from the cart window it is actually removed"""
        for i in range(2):
            self.homepage.enter_category()
            self.category.click_product()
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            self.product.add_to_cart()
            self.general.click_the_logo()
        products_in_cart = len(self.general.products_in_cart_window())
        self.general.remove_product_from_cart_window()
        self.assertEqual(products_in_cart-1, len(self.general.products_in_cart_window()))

    def test_4_left_shopping_cart(self):
        """Test that cart page opens as should"""
        self.homepage.enter_category()
        self.category.click_product()
        self.product.add_to_cart()
        rand = randint(0, 9)
        self.product.add_quantity(rand)
        self.product.add_to_cart()
        self.general.click_cart()
        self.assertTrue(self.general.find_location_navigationline() == "SHOPPING CART")

    def test_5_right_sum_in_cart(self):
        """Test that the sum of the order is the same in the total price in the cart and if calculated in the test"""
        test_sum = 0
        for i in range(3):
            self.homepage.enter_category()
            self.category.click_product()
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            product_price = self.product.product_price()
            test_sum += (rand + 1) * product_price
            self.product.add_to_cart()
            print(f"in the product page:\nthe name of the product is: {self.product.product_name()}, it's quantity is: {rand+1} and it's price is: {product_price} ")
            self.general.click_the_logo()
        self.general.click_cart()
        products_names = self.cart.products_names()
        products_quantities = self.cart.products_quantities()
        products_prices = self.cart.products_price()
        for p in range(len(products_names)):
            print(f"in the cart page:\nthe name of the product is: {products_names[p]}, it's quantity is: {products_quantities[p]} and it's price is: {products_prices[p]} ")

        self.assertEqual(self.cart.total_price(), test_sum)

    def test_6_edit_cart(self):
        """Test that checks if edit the quantity of the products in the cart really changes the quantity in the cart"""
        for i in range(2):
            self.homepage.enter_category()
            self.category.click_product()
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            self.product.add_to_cart()
            self.general.click_the_logo()
            self.general.click_cart()
            ActionChains(self.driver).move_to_element(self.general.find_username()).perform()
            self.cart.click_edit(0)
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            self.product.add_to_cart()
            self.cart.click_edit(1)
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            self.general.click_cart()
            self.assertEqual(self.product.product_quantity(0), self.cart.products_quantities()[0])
            self.assertEqual(self.product.product_quantity(1), self.cart.products_quantities()[1])

    def test_7_tablets_path(self):
        """Test the path from product to the home page in tablets category"""
        self.homepage.enter_category()
        while self.category.category_headline() != 'TABLETS':
            self.general.click_the_logo()
            self.homepage.enter_category()
        self.category.click_product()
        self.driver.back()
        self.assertTrue(self.category.category_headline() == 'TABLETS')
        self.assertTrue(self.general.find_location_navigationline() == 'TABLETS')
        self.driver.back()
        self.assertEqual(self.driver.current_url, "https://www.advantageonlineshopping.com/#/")

    def test_8_order_new_user(self):
        """Test that order completes successfully while the user is created in the presses """
        for i in range(randint(2, 4)):
            self.homepage.enter_category()
            self.category.click_product()
            rand = randint(0, 9)
            self.product.add_quantity(rand)
            self.product.add_to_cart()
            self.general.click_the_logo()
        self.general.click_cart()
        self.cart.click_checkout()
        self.general.click_register_in_checkout()
        self.create_account.fill_username("LeonGaya65")
        self.create_account.fill_email("LeonGaya65@gmail.com")
        self.create_account.fill_passwords("LeonGaya65!")
        self.create_account.register()
        self.payment.click_next_in_OrderPayment()
        self.payment.fill_safepay_username("LeonGaya651")
        self.payment.fill_safepay_password("LeonGaya651")
        self.payment.click_pay_now_safepay()
        self.assertTrue(self.general.order_message())
        self.general.click_cart()
        # self.assertEqual(self.cart.empty_cart_message().text, "Your shopping cart is empty")
        self.assertTrue(self.cart.zero_items_in_cart() == 0)
        self.general.click_my_orders()
        self.assertIsNotNone(self.general.find_order_number())
        self.general.click_my_account()
        self.general.click_delete_account()

    def test_10_login_signout(self):
        """Test that the login and log out process of already existed account are done successfully """
        self.general.click_user_logo()
        self.homepage.username()
        self.homepage.fill_username("leonk1")
        self.homepage.password()
        self.homepage.fill_password("Ll12345")
        self.homepage.click_signin()
        self.assertEqual(self.general.find_username().text, "leonk1")
        self.general.click_username()
        self.homepage.click_user_signout()
        self.general.click_user_logo()
        self.assertEqual(self.homepage.username().text, "")
