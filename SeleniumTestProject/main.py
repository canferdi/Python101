import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window() #Tam ekranda açar

driver.get("https://www.google.com/") #google.com'a gider

WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))
inputElementByName = driver.find_element(By.NAME, "q")  #Ekrandaki elemanı bulur
inputElementByName.send_keys("Ege Bilgisayar Mühendisliği")   #Ekrandaki textboxa yazar

#time.sleep(0.5)
#Buton tıklanabilir olana kadar bekle
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "btnK")))
searchButton = driver.find_element(By.NAME, "btnK")
searchButton.click()  #Butona tıklar

time.sleep(10) #10'sn bekle sonra kapan
#while True:
#  continue   #Kapatılana kadar açık kalır