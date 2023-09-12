import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import page

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		self.driver.get("http://www.python.org")													#change website here

	def tearDown(self):
		self.driver.quit()


	def test_search_python(self):																	#change test
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()
		mainPage.search_text_element = "pycon"
		mainPage.click_go_button()
		search_result_page = page.SearchResultPage(self.driver)
		assert search_result_page.is_results_found()

	def test_psf_tab(self):																			#change test
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()
		mainPage.click_psf_tab_button()
		psfTabPage = page.PsfTabPage(self.driver)
		assert psfTabPage.is_title_matches()



if __name__ == '__main__':
	unittest.main(exit=False)