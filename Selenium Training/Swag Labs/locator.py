from selenium.webdriver.common.by import By


class MainPageLocators(object):
	USERNAME = (By.ID, "user-name")					#change locators here
	PASSWORD = (By.ID, "password")					#change locators here
	LOGIN_BUTTON = (By.ID, "login-button")
	ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")


class CatalogPageLocators(object):
	SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
	INVENTORY_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
	INVENTORY_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
	CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge")
	INVENTORY_ITEM_ADD_BUTTONS = (By.CLASS_NAME, "btn_inventory")
