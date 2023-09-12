from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

def ElementClick(num, object):
    for i in range(num):
        object.click()
        count_text = int(count.text.split(' ')[0])
        for item in items:
            value = int(item.text)
            if count_text >= value:
                clickItemActions = ActionChains(driver)
                clickItemActions.move_to_element(item)
                clickItemActions.click()
                clickItemActions.perform()
        #time.sleep(0.05)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.maximize_window()

time.sleep(5)

language = driver.find_element(By.ID, "langSelect-EN")
language.click()

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")
count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range (1,-1,-1)]

while 1==1:
    ElementClick(20, cookie)