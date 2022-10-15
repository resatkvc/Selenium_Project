from selenium import webdriver

driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.amazon.com/')

Link = driver.current_url
baslik =driver.title
print('Sayfa Baslığı:'+baslik)
driver.save_screenshot('./amazonekrangoruntusu.png')

driver.quit()

