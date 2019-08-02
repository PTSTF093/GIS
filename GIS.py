#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time
import datetime
#import getpass
#user = input('User:')
#pass = getpass.getpass('Password:')

driver = webdriver.Firefox()

#https://vpn.montepio.pt/+CSCOE+/portal.html
driver.get('https://vpn.montepio.pt/+CSCOE+/logon.html')

print driver.title

assert 'Montepio' in driver.title

elem_u = driver.find_element_by_name('username')  # Find the usernme box
elem_u.send_keys('Z0356')
elem_p = driver.find_element_by_name('password')  # Find the usernme box
elem_p.send_keys('x22tGQ<g' + Keys.RETURN)



#esperar um pouco
time.sleep(5)

#aguardar nova pagina
WebDriverWait(driver, 10).until(EC.title_contains("Montepio"))
print driver.title

#frame = driver.find_element_by_tag_name("a")
#frame.click()

#FTPM = driver.find_element_by_link_text("FTP MONITOR")
#FTPM = driver.find_element_by_partial_link_text("FTP") FTP MONITOR
#FTPM = driver.find_element(By.PARTIAL_LINK_TEXT, "MONITOR")
#FTPM.click()

#https://vpn.montepio.pt/+CSCOE+/portal.html
driver.get('https://vpn.montepio.pt/+CSCO+00756767633A2F2F7367637A6261766762652E7A626167726376622E70627A++/')
#aguardar nova pagina
WebDriverWait(driver, 10).until(EC.title_contains("FTPMonitor"))
print driver.title

#loop infinito
while True:
	#cmdActiveReport
	elem_botao = driver.find_element_by_name('cmdActiveReport')
	elem_botao.click()
	now = datetime.datetime.now()
	print "refresh efetuado " + str(now)[:19] #print str(now)[:19]
	time.sleep(60)
	#driver.submit()
	#driver.get('https://vpn.montepio.pt/+CSCO+00756767633A2F2F7367637A6261766762652E7A626167726376622E70627A++/')
	

#driver.quit()
