from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

username = ''
password = ''

# Search selenium ChromeDriver or Firefox / and download deiver in folder project
driver = webdriver.Firefox()  #Open Brawser Firefox
driver.get('https://www.instagram.com/accounts/login/')
sleep(6)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
sleep(5)
driver.find_element_by_name('password').send_keys(Keys.RETURN) # click inter
sleep(5)
driver.get('https://www.instagram.com/'+'therock') # move to page rock
sleep(5)
follw_btn = driver.find_element(By.XPATH, '//button[text()="Follow"]') # find but
sleep(5)
follw_btn.click() # click Button
sleep(7)
driver.refresh() # refresh page


