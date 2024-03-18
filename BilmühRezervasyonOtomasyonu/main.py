import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeH0LZu4yacwlPsvias3J1L7GUqS6XuDQH5eKD6EsODEjqheA/viewform") #google.com'a gider

path = "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
input = driver.find_element(By.XPATH, path)
time.sleep(1)
input.send_keys("Ferdi")

path = "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
input = driver.find_element(By.XPATH, path)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
input.send_keys("Can")

path = "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
input = driver.find_element(By.XPATH,path )
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
input.send_keys("05220000957")

path="/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input"
input = driver.find_element(By.XPATH,path )
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
input.send_keys(".")

path = "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input"
input = driver.find_element(By.XPATH, path)
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
input.send_keys(".")

path = "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span"
input = driver.find_element(By.XPATH, path)
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, path)))
input.click()

time.sleep(10)