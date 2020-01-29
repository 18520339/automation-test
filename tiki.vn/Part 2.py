from selenium import webdriver
import time

## B1. WebDriver - WebBrowser
driver = webdriver.Firefox()

driver.get('https://tiki.vn/')

## Form Obj 01
time.sleep(5)
uiLinkDT = driver.find_element_by_xpath("//li[@class='MenuItem-tii3xq-0 krWJFU'][1]")
uiLinkDT.click()

## Form Obj 02
time.sleep(5)
uiQuery = driver.find_element_by_xpath("//input[@name='q']")
uiS01 = driver.find_element_by_xpath("//div[@class='search-wrap']//button")
uiQuery.send_keys('samsung')
uiS01.click()

## Form Obj 03
uiMIN = driver.find_element_by_xpath("//input[@class='slide-input slide-from']")
uiMAX = driver.find_element_by_xpath("//input[@class='slide-input slide-to']")
uiSearchBtn = driver.find_element_by_xpath("//button[@id='price-slider-submit']")

uiMIN.send_keys("30000000")
uiMAX.send_keys("50000000")
uiSearchBtn.click()

time.sleep(5)
print('Done !')