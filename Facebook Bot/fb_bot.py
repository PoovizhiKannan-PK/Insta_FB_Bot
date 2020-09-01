from selenium import webdriver
from time import sleep
from password import pw
#//button[contains(text(),'Log In')]


class fb_bot:

	def __init__(self, uname, pw):
		self.option = webdriver.ChromeOptions()
		self.option.add_argument('--disable-notifications')
		self.uname = uname
		self.pw = pw
		self.driver = webdriver.Chrome(options=self.option)
		self.driver.get('https://www.facebook.com/')
		self.driver.maximize_window()
		sleep(1)
		self.driver.find_element_by_id('email').send_keys(uname)
		self.driver.find_element_by_id('pass').send_keys(pw)
		#self.driver.find_element_by_xpath('//input[@name=\'email\']').send_keys(uname)
		#self.driver.find_element_by_xpath('//input[@name=\'pass\']').send_keys(pw)
		self.driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
		sleep(2)
		sleep()

	def scroll_page(self):
		self.minus = 1500
		self.initial_ht = int(self.driver.execute_script("return document.body.scrollHeight"))
		print(self.initial_ht)

		while(True):	
			self.driver.execute_script("window.scrollTo(0, Number(document.body.scrollHeight)-self.minus)")	
			print(self.driver.execute_script("Number(document.body.scrollHeight)"))
			print(self.driver.execute_script("Number(self.minus)"))
			print(self.driver.execute_script("self.minus"))
			sleep(2)
			self.current_ht = int(self.driver.execute_script("return document.body.scrollHeight"))-self.minus
			if(self.initial_ht == self.current_ht):
				break;
			self.initial_ht = self.current_ht
			


facebook = fb_bot('poovizhikannan370@gmail.com', pw)

facebook.scroll_page()