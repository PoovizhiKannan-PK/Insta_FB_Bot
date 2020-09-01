from selenium import webdriver
from time import sleep

class test:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get('https://pythonbasics.org/selenium-scroll-down/')
		self.driver.execute_script('0, document.body.scrollHeight')

test()