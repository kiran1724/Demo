from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('http://stackoverflow.com')
print("Title: "+ str(driver.title))
print("Closing driver")
driver.quit()

