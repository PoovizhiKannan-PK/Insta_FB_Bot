import selenium
from selenium import webdriver
import time

class instabot:
	def __init__(self, uname, password):
		self.driver = webdriver.Chrome()
		self.uname = uname
		self.driver.get('https://www.instagram.com/')
		self.driver.maximize_window()
		time.sleep(3)
		self.driver.find_element_by_xpath('//input[@name=\'username\']').send_keys(uname)
		self.driver.find_element_by_xpath('//input[@name=\'password\']').send_keys(password)
		self.driver.find_element_by_xpath('//button[@type = \'submit\']').click()
		time.sleep(3)
		self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
		time.sleep(2)

	def scroll_page(self):
		'''
		scroll_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main')
		ht, last_ht = 0,1000
		while ht != last_ht:
			last_ht = ht
			time.sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0,arguments[0].scrollHeight + 1000);
				return arguments[0].scrollHeight;
				""", scroll_box)
		#print("Here")
		#self.i =0
		#self.j=1000
		#while(1):
		#self.driver.execute_script("window.scrollTo(0,10000)")
		#	self.i=self.j
		#	self.j=self.j+1000
		#	time.sleep(2)
		
		ht = document.body.scrollHeight()
		last_ht= 200
		while(1):
			window.scrollTo(ht, last_ht)
			ht = last_ht
			last_ht = last_ht+200

		
		'''
		self.initial_ht = int(self.driver.execute_script("return document.body.scrollHeight"))
		ht = self.driver.execute_script("return document.body.scrollHeight")
		print(int(ht))

		while(True):	
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")	
			time.sleep(2)
			self.current_ht = int(self.driver.execute_script("return document.body.scrollHeight"))
			if(self.initial_ht == self.current_ht):
				print('here')
				break;
			self.initial_ht = self.current_ht
			

	def get_followers(self):
		time.sleep(2)
		self.driver.find_element_by_xpath("//a[contains(text(),'poovizhikannan003')]").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
		time.sleep(2)
		scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
		ht, last_ht = 0,1
		while ht != last_ht:
			last_ht = ht
			time.sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0,arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)
			"""b
			#for i in range(100):
			names = scroll_box.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a')
			#names = [name.session for name in links]
			with open ('names.txt', 'w') as f:
				for items in names:
					f.write("%s\n" % items)
			"""


insta_bot = instabot('poovizhikannan003', '#Your password Here#')

insta_bot.scroll_page()
#insta_bot.get_followers()