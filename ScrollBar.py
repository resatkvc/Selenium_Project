from selenium import webdriver

driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.nationalgeographic.com/')

# Scroll down page by pixel (Scroll barı hareket ettirme sayfa içerisinde piksel belirterek)

# driver.execute_script("window.scrollBy(0,200)","")
# time.sleep(2)
# print("\t5-Sayfa aşağıya doğru kaydırma işlemi başarılı şekilde yapıldı")

# Scroll down page till the element is visible (sayfada isteğimiz kısma scrol bar ile doğrudan o kısmı gösterme)

#Travel=driver.find_element (By.XPATH, '//*[@id="c9f58879-5d98-415d-92c6-4834ff8e081f"]/div/h2')
#driver.execute_script("arguments[0].scrollIntoView();",Travel)

# Scroll Down Page (sayfanın sonuna gelir)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.quit()
