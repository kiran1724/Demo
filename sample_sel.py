from selenium import webdriver

desiredCapabilities={
"browserName":"chrome"
}

driver = webdriver.Remote(desired_capabilities=desiredCapabilities, 
			command_executor='http://10.0.2.15:4444/wd/hub')
driver.get('https://www.amazon.in/')
print("Title: "+ str(driver.title))
print("Closing driver")
driver.quit()

