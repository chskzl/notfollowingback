from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

account = "accountname"
passwd = "password"

class NotFollowingBack():
	def __init__(self):
		self.driver = webdriver.Firefox()

	def run(self):
		self.driver.get('https://instagram.com')

		sleep(2)

		uname_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
		uname_in.send_keys(account)

		pw_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
		pw_in.send_keys(passwd)

		login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
		login_button.click()

		sleep(5)

		self.driver.get('https://instagram.com/' + account)

		followers = []
		following = []
		doesntfollowback = []

		numfollowers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
		numfollowing = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
		print("numfollowers = " + numfollowers)
		print("numfollowing = " + numfollowing)

		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()

		sleep(1)

		for i in range(1, int(numfollowers) + 1):
			try:
				followers.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a').text)
			except Exception:
				try:
					followers.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/span/a').text)
				except Exception:
					try:
						self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i-1)+']/div/div[2]/div[1]/div/div/span/a').send_keys(Keys.PAGE_DOWN)
					except Exception:
						self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i-1)+']/div/div[1]/div[2]/div[1]/span/a').send_keys(Keys.PAGE_DOWN)
					sleep(1)
					try:
						followers.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a').text)
					except Exception:
						followers.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/span/a').text)

		self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()

		sleep(1)

		for i in range(1, int(numfollowing) + 1):
			try:
				following.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a').text)
			except Exception:
				try:
					following.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/span/a').text)
				except Exception:
					try:
						self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i-1)+']/div/div[2]/div[1]/div/div/span/a').send_keys(Keys.PAGE_DOWN)
					except Exception:
						self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i-1)+']/div/div[1]/div[2]/div[1]/span/a').send_keys(Keys.PAGE_DOWN)
					sleep(1)
					try:
						following.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/span/a').text)
					except Exception:
						following.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/span/a').text)

		self.driver.close()

		for i in range(int(numfollowing)):
			if following[i] not in followers:
				print(following[i])
	
bot = NotFollowingBack()
bot.run()
