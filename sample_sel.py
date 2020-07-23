print("-------Line 1-------")
print("####################")
print("-------Line 2-------")

import os
print("Current directory: " + str(os.getcwd()))

from selenium import webdriver

desiredCapabilities={
"browserName":"chrome"
}

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromedriver'

#driver = webdriver.Remote(desired_capabilities=desiredCapabilities, 
#			command_executor='http://10.0.2.15:5555/wd/node')
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.amazon.in/')
print("Title: "+ str(driver.title))
print("Closing driver")
driver.quit()

