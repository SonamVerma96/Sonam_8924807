# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up the webdriver
driver = webdriver.Chrome()

#Redirect to the ecommerce website- ebay
driver.get("https://www.ebay.com/signin/?sgn=reg&siteid=0")
time.sleep(3)

#Input username
username_field = driver.find_element("id", 'userid')
username_field.send_keys('vsonam996@gmail.com')

#click on continue button
continueBtn = driver.find_element("id", "signin-continue-btn")
continueBtn.click()
time.sleep(2)

# #Input password
password_field = driver.find_element("id", 'pass')
password_field.send_keys('Sonam@123')

#click on Sign in button
signBtn = driver.find_element("id", "sgnBt")
signBtn.click()
time.sleep(2)

#May be Later Button
maybelaterBtn = driver.find_element("id", "webauthn-maybe-later-link")
maybelaterBtn.click()
time.sleep(2)

#Redirected to the Main Home Page of the website
WebDriverWait(driver, 10).until(EC.url_contains("https://www.ebay.com/"))

# Click on daily deals
ebayDeal = driver.find_element("id", "gh-p-1")
ebayDeal.click()
time.sleep(2)

#click the image
dealImg = driver.find_element("xpath", "/html/body/main/div/div[2]/div[1]/div[3]/div/div[6]/div/a/div/div/img")
dealImg.click()
time.sleep(3)

#check the details of image
imgDetail = driver.find_element("id", "x-msku__select-box-1000")
imgDetail.click()
time.sleep(2)

#check the details of image
imgDetail1 = driver.find_element("id", "x-msku__option-box-0")
imgDetail1.click()
time.sleep(2)

# #check the details of image
imgDetail2 = driver.find_element("id", "x-msku__select-box-1001")
imgDetail2.click()
time.sleep(2)

imgDetail3 = driver.find_element("id", "x-msku__option-box-4")
imgDetail3.click()
time.sleep(2)


addtocart = driver.find_element("xpath", "/html/body/div[5]/div[3]/div/div/div[3]/div[3]/div[2]/form/div[2]/div/div[1]/div[2]/ul/li[2]/div/a/span/span")
addtocart.click()
time.sleep(3)

removefromcart = driver.find_element("xpath", "/html/body/div[5]/div[2]/div/div[2]/div[1]/div[1]/div/ul/li/div/div/div/div[2]/span[2]/button")
removefromcart.click()
time.sleep(3)

# checkList = driver.find_element("xpath", "/html/body/div[7]/div[3]/div/div[2]/div[4]/div[3]/div[1]/div[2]/div/span/input")
# checkList.click()
# time.sleep(2)
#
# checkList1 = driver.find_element("xpath", "/html/body/div[7]/div[3]/div/div[2]/div[4]/div[1]/div[1]/ul/li[3]/div/button")
# checkList1.click()
# time.sleep(2)
#
# signout = driver.find_element("xpath","/html/body/div[5]/div[2]/div/div/header/div/ul[1]/li[1]/button")
# signout.click()
# time.sleep(2)
#
# signout1 = driver.find_element("/html/body/div[5]/div[2]/div/div/header/div/ul[1]/li[1]/div/ul/li[5]/a")
# signout1.click()
# time.sleep(2)


# Closing the webdriver
driver.close()
