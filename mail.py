import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\chromedriver.exe')
driver.get('https://mail.tm/tr/')
driver.maximize_window()
    
a = driver.get_cookie('auth._token.local')['value']



copyButton = driver.find_element_by_xpath('//*[@id="accounts-menu"]')

copyButton.click()


mail = driver.find_element_by_xpath('//*[@id="accounts-list"]/div/div[1]/p[2]').text
token = driver.get_cookie('auth._token.local')['value']
token=token.replace("%20"," ")

dosya = open('info/token.txt', 'w')
dosya.write(token) 
dosya.close()

dosya = open('info/mail.txt', 'w')
dosya.write(mail) 
dosya.close()

driver.quit()









