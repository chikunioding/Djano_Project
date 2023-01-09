import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\Django_Project001\driver\chromedriver.exe")
driver.get(r"https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()
time.sleep(2)

a=driver.find_element(By.XPATH,"//input[@name='firstname']")
a.send_keys("Hiraman")
a.send_keys(Keys.CONTROL+'a')
a.send_keys(Keys.CONTROL+'c')

b=driver.find_element(By.XPATH,"//input[@name='lastname']")
b.send_keys(Keys.CONTROL+'v')
