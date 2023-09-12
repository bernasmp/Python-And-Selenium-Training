from locator import MainPageLocators
from locator import CatalogPageLocators
from selenium.webdriver.support.ui import Select


# from element import BasePageElement

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Swag Labs" in self.driver.title

    def is_username_label_matches(self):
        username = self.driver.find_element(*MainPageLocators.USERNAME)
        usernamePlaceholder = username.get_attribute("placeholder")
        return usernamePlaceholder == "Username"

    def is_password_label_matches(self):
        password = self.driver.find_element(*MainPageLocators.PASSWORD)
        passwordPlaceholder = password.get_attribute("placeholder")
        return passwordPlaceholder == "Password"

    def insert_username(self):
        username = self.driver.find_element(*MainPageLocators.USERNAME)
        username.send_keys("standard_user")

    def insert_password(self):
        password = self.driver.find_element(*MainPageLocators.PASSWORD)
        password.send_keys("secret_sauce")

    def click_login_button(self):
        loginButton = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        loginButton.click()

    def is_error_message(self):
        try:
            errorMessage = self.driver.find_element(*MainPageLocators.ERROR_MESSAGE)
            return "Epic sadface" in errorMessage.text
        except:
            pass


class CatalogPage(BasePage):

    def is_title_matches(self):
        return "Swag Labs" in self.driver.title

    def is_url_matches(self):
        url = self.driver.current_url
        return url == "https://www.saucedemo.com/inventory.html"

    def dropdown_select_az(self):
        drp = Select(self.driver.find_element(*CatalogPageLocators.SORT_DROPDOWN))
        drp.select_by_visible_text("Name (A to Z)")

    def dropdown_select_za(self):
        drp = Select(self.driver.find_element(*CatalogPageLocators.SORT_DROPDOWN))
        drp.select_by_visible_text("Name (Z to A)")

    def dropdown_select_lohi(self):
        drp = Select(self.driver.find_element(*CatalogPageLocators.SORT_DROPDOWN))
        drp.select_by_visible_text("Price (low to high)")

    def dropdown_select_hilo(self):
        drp = Select(self.driver.find_element(*CatalogPageLocators.SORT_DROPDOWN))
        drp.select_by_visible_text("Price (high to low)")

    def check_items_az(self):
        item_list = self.driver.find_elements(*CatalogPageLocators.INVENTORY_ITEM_NAMES)
        for i in range(len(item_list)):
            item_list[i] = item_list[i].text
        for i in range(len(item_list) - 1):
            if item_list[i] > item_list[i + 1]:
                return False
        return True

    def check_items_za(self):
        item_list = self.driver.find_elements(*CatalogPageLocators.INVENTORY_ITEM_NAMES)
        for i in range(len(item_list)):
            item_list[i] = item_list[i].text
        for i in range(len(item_list) - 1):
            if item_list[i] < item_list[i + 1]:
                return False
        return True

    def check_items_lohi(self):
        item_list = self.driver.find_elements(*CatalogPageLocators.INVENTORY_ITEM_PRICES)
        for i in range(len(item_list)):
            item_list[i] = item_list[i].text
            item_list[i] = item_list[i][1:]
            item_list[i] = float(item_list[i])
        for i in range(len(item_list) - 1):
            if item_list[i] > item_list[i + 1]:
                return False
        return True

    def check_items_hilo(self):
        item_list = self.driver.find_elements(*CatalogPageLocators.INVENTORY_ITEM_PRICES)
        for i in range(len(item_list)):
            item_list[i] = item_list[i].text
            item_list[i] = item_list[i][1:]
            item_list[i] = float(item_list[i])
        for i in range(len(item_list) - 1):
            if item_list[i] < item_list[i + 1]:
                return False
        return True

    def click_item(self, item):
    	item_list = self.driver.find_elements(*CatalogPageLocators.INVENTORY_ITEM_ADD_BUTTONS)
    	item_selected = item_list[item]
    	item_selected.click()

    def read_cart_number(self):
    	cart_number = self.driver.find_element(*CatalogPageLocators.CART_NUMBER)
    	return cart_number.text

    def read_item_button(self, item):
    	item_list = self.driver.find_elements(*CatalogPageLocators.INVENTORY_ITEM_ADD_BUTTONS)
    	item_button = item_list[item]
    	return item_button.text
