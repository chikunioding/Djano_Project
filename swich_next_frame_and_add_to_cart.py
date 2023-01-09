import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\Django_Project001\driver\chromedriver.exe")
driver.get(r"https://www.flipkart.com/")

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()

action=ActionChains(driver)
a=driver.find_element(By.XPATH,"//div[text()='Fashion']")
action.move_to_element(a)
action.perform()
time.sleep(2)

b=driver.find_element(By.XPATH,"//a[text()='Women Western']")
action.move_to_element(b)
action.perform()
time.sleep(2)

c=driver.find_element(By.XPATH,"//a[text()='Women T-shirts & Polo T-shirts']")
action.move_to_element(c)
action.click().perform()

parent=driver.current_window_handle
print(parent)

driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a/div[1]/div/div/div/img").click()
time.sleep(2)

childtab=driver.window_handles
print(childtab)

for i in childtab:
    if i !=parent:
        driver.switch_to.window(i)
        time.sleep(5)
        driver.find_element(By.XPATH,"//a[text()='M']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()









