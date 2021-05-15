from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


usrname = []

import csv
with open('Copy of Influencers_health.csv', 'r',encoding="utf8") as file:
	reader = csv.reader(file)
	for row in reader:
		row1 = row[1]
		if row1 == 'username':
			pass
		else:
			usrname.append(row1)
		
print((usrname))
def Direct_Message():
    usrnames = usrname 
    geckodriver = 'C:\\Users\\sa\\Desktop\\mathew\\geckodriver.exe'
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    binary = FirefoxBinary('C:\\Users\\sa\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
    browser = webdriver.Firefox(executable_path=geckodriver,firefox_options=options,firefox_binary=binary)
    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')
    username = 'john20.21' 
    password = 'puneet@6644' 
    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)
    time.sleep(11)
    def send_msg(usrnames):
        print("999998")
        browser.get('https://www.instagram.com/direct/new/')
        time.sleep(5)
        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usrnames)
        time.sleep(8)
        nxtbtn = browser.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
        nxtbtn.click()
        time.sleep(3)
        chk_mrk = browser.find_element_by_class_name('dCJp8')
        chk_mrk.click()
        time.sleep(3)
		
        try:
            nxt_btn = browser.find_element_by_xpath('//div[@class="rIacr"]')
            nxt_btn.click()
        except:
           pass
        try:
            nxt_btn = browser.find_element_by_xpath('//div[@class="sqdOP yWX7d    y3zKF   cB_4K"]')
            nxt_btn.click()
        except:
            pass
		  
        time.sleep(6)
        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys('Hey! I noticed your Pilates classes listed on your profile and thought I’d reach out to tell you about HeyExpert: HeyExpert is an exciting online platform that helps Pilates business owners like you manage and grow their business, risk and hassle free. We are offering this platform for free with zero subscription fees. If this sounds up your alley, check here to learn more about how our platform works and what it can do for you: https://bit.ly/2SwB5sL Looking forward to having you join us')  
        time.sleep(2)
        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()
        time.sleep(4)
    count = 0
    try:
        for usrnamee in usrnames:
            print("888")
            send_msg(usrnamee)
            count += 1
    except :
        print('Failed!')

    browser.quit()

    print(f'''Successfully Sent {count} Direct Massages to the User''')

if __name__ == '__main__':
	obj = Direct_Message()

