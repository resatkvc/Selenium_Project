from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://duckduckgo.com/")
time.sleep(1)

Search = driver.find_element(By.ID, "search_form_input_homepage")
Search.send_keys("Selenium")
Input = driver.find_element(By.ID, 'search_button_homepage')
Input.click()
time.sleep(1)

SeleiumDocument= driver.find_element(By.CSS_SELECTOR, "#sl-2 > a > h3")
SeleiumDocument.click()
driver.quit()
