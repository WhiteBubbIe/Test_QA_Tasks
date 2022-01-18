from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.google.ru/')
searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('first video on youtube')

searchButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
searchButton.click()