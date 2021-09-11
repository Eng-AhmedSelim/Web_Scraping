from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

username = ''
password = ''


def scrappe():
    driver = webdriver.Firefox()
    driver.get('https://flat.io/auth/signin?hl=en')
    driver.find_element(By.ID, "emailInput").send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    print('Successfully logged In .....')
    sleep(3)
    driver.get('https://flat.io/popular/')
    print('Navigating To Poplar Tracks ..')
    sleep(10)

    print('Scrolling ----->')
    for i in range(1, 1000):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)
        print("try agne")


scrappe()
