import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.imdb.com")
#Menüye tıklatmada bir değişkene atamamamızın sebebi bir daha kullanmayacak olmamız.o yüzden değişkene atamadan doğrudan elementi tıklatıyoruz
driver.find_element(By.ID, "imdbHeader-navDrawerOpen--desktop").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()

#Film adını yazdırır

#MoveNames = driver.find_elements(By.XPATH, "//table/tbody//tr//td[@class='titleColumn']/a")
#Listedeki ilk 20 film listesini yazdır
#for i in range(20):
    #print(MoveNames[i].text)

#Film adını ve yılını yazdırır.

#MoveNames = driver.find_elements(By.XPATH, "//table/tbody//tr//td[@class='titleColumn']")
#for i in range(20):
    #print(MoveNames[i].text)


MoveNames = driver.find_elements(By.XPATH, "//table/tbody//tr//td[@class='titleColumn']")
#Yıllar parantez içerisinde oldugundan dolayı -5 ile -1 arasındaki yılı 2021 olan filmleri yazdırır
for i in MoveNames:
    if i.text[-5:-1] == "2021":  
        print(i.text)

driver.quit()
