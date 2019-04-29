from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://wifiology.copesystems.com")


username = driver.find_element_by_id('inputUsername')
username.send_keys("chen")
username = driver.find_element_by_id('inputPassword')
username.send_keys("123456")

sleep(1)
login = driver.find_element_by_xpath("//button[contains(text(),'Log in')]")
login.click()
sleep(1)
click = driver.find_element_by_xpath("/html/body/nav/button[1]")
click.click()
sleep(1)
logout = driver.find_element_by_xpath("//a[contains(text(),'Logout')]")
logout.click()
