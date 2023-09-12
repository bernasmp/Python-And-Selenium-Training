from selenium.webdriver.common.by import By

class MainPageLocators(object):
	GO_BUTTON = (By.ID, "submit")					#change locators here
	PSF_TAB_BUTTON = (By.LINK_TEXT, "PSF")			#change locators here

class SearchResultsPageLocators(object):
	pass