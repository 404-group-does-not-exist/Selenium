from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://wifiology.copesystems.com")

register = driver.find_element_by_xpath("//a[contains(text(),'Register')]")
register.click()

username = driver.find_element_by_id('username')
username.send_keys("test03")
username = driver.find_element_by_id('emailAddress')
username.send_keys("test3@copesystems.com")
username = driver.find_element_by_id('password')
username.send_keys("123456")
username = driver.find_element_by_id('passwordConfirm')
username.send_keys("123456")

sleep(1)
register2 = driver.find_element_by_xpath("//button[contains(text(),'Register')]")
register2.click()
sleep(1)
click = driver.find_element_by_xpath("/html/body/nav/button[1]")
click.click()
sleep(1)
logout = driver.find_element_by_xpath("//a[contains(text(),'Logout')]")
logout.click()
sleep(1)

username = driver.find_element_by_id('inputUsername')
username.send_keys("test03")
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
