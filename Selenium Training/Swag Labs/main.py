import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import page


class SwagLabsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		self.driver.get("https://www.saucedemo.com/")

	def tearDown(self):
		self.driver.quit()

	def test_title_matches(self):
		print("--Home Page title matches--")
		mainPage = page.MainPage
		assert mainPage.is_title_matches(self)

	def test_login_placeholders(self):
		print("--Correct login placeholders--")
		mainPage = page.MainPage
		assert mainPage.is_username_label_matches(self)
		assert mainPage.is_password_label_matches(self)

	def test_successful_login(self):
		print("--Successful Login--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		assert not mainPage.is_error_message(self)
		assert catalogPage.is_title_matches(self)
		assert catalogPage.is_url_matches(self)

	def test_unsuccessful_login(self):
		print("--Unsuccessful Login--")
		mainPage = page.MainPage
		mainPage.click_login_button(self)
		assert mainPage.is_error_message(self)

	def test_sort_az(self):
		print("--Sort Items A to Z--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		catalogPage.dropdown_select_az(self)
		assert catalogPage.check_items_az(self)

	def test_sort_za(self):
		print("--Sort Items Z to A--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		catalogPage.dropdown_select_za(self)
		assert catalogPage.check_items_za(self)

	def test_sort_lohi(self):
		print("--Sort Items Low to High--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		catalogPage.dropdown_select_lohi(self)
		assert catalogPage.check_items_lohi(self)

	def test_sort_hilo(self):
		print("--Sort Items High to Low--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		catalogPage.dropdown_select_hilo(self)
		assert catalogPage.check_items_hilo(self)

	def test_add_item_cart_badge(self):
		print("--Shopping Cart Badge--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		catalogPage.click_item(self, 0)
		assert catalogPage.read_cart_number(self) == "1"
		catalogPage.click_item(self, 1)
		assert catalogPage.read_cart_number(self) == "2"
		catalogPage.click_item(self, 2)
		assert catalogPage.read_cart_number(self) == "3"
		catalogPage.click_item(self, 3)
		assert catalogPage.read_cart_number(self) == "4"
		catalogPage.click_item(self, 4)
		assert catalogPage.read_cart_number(self) == "5"
		catalogPage.click_item(self, 5)
		assert catalogPage.read_cart_number(self) == "6"
		catalogPage.click_item(self, 0)
		assert catalogPage.read_cart_number(self) == "5"
		catalogPage.click_item(self, 1)
		assert catalogPage.read_cart_number(self) == "4"
		catalogPage.click_item(self, 2)
		assert catalogPage.read_cart_number(self) == "3"
		catalogPage.click_item(self, 3)
		assert catalogPage.read_cart_number(self) == "2"
		catalogPage.click_item(self, 4)
		assert catalogPage.read_cart_number(self) == "1"

	def test_add_item_button_text(self):
		print("--Add/Remove Item Button Text--")
		mainPage = page.MainPage
		catalogPage = page.CatalogPage
		mainPage.insert_username(self)
		mainPage.insert_password(self)
		mainPage.click_login_button(self)
		catalogPage.click_item(self, 0)
		assert catalogPage.read_item_button(self, 0) == "REMOVE"
		catalogPage.click_item(self, 1)
		assert catalogPage.read_item_button(self, 1) == "REMOVE"
		catalogPage.click_item(self, 2)
		assert catalogPage.read_item_button(self, 2) == "REMOVE"
		catalogPage.click_item(self, 3)
		assert catalogPage.read_item_button(self, 3) == "REMOVE"
		catalogPage.click_item(self, 4)
		assert catalogPage.read_item_button(self, 4) == "REMOVE"
		catalogPage.click_item(self, 5)
		assert catalogPage.read_item_button(self, 5) == "REMOVE"
		catalogPage.click_item(self, 0)
		assert catalogPage.read_item_button(self, 0) == "ADD TO CART"
		catalogPage.click_item(self, 1)
		assert catalogPage.read_item_button(self, 1) == "ADD TO CART"
		catalogPage.click_item(self, 2)
		assert catalogPage.read_item_button(self, 2) == "ADD TO CART"
		catalogPage.click_item(self, 3)
		assert catalogPage.read_item_button(self, 3) == "ADD TO CART"
		catalogPage.click_item(self, 4)
		assert catalogPage.read_item_button(self, 4) == "ADD TO CART"
		catalogPage.click_item(self, 5)
		assert catalogPage.read_item_button(self, 5) == "ADD TO CART"


if __name__ == '__main__':
	unittest.main(exit=False)
