import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\Django_Project001\driver\chromedriver.exe")
driver.get(r"https://www.flipkart.com/")

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()

action=ActionChains(driver)

a1=driver.find_element(By.XPATH,"//div[text()='Electronics']")
action.move_to_element(a1)
time.sleep(2)
driver.implicitly_wait(5)
b1=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[4]/a/div[2]/div[2]/div[2]/div/div/div[1]/a[4]")
action.move_to_element(b1)
time.sleep(2)

c1=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[4]/a/div[2]/div[2]/div[2]/div/div/div[2]/a[4]")
action.move_to_element(c1)
action.click().perform()