#!/usr/bin/python
# -*- coding: latin-1 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException
import easygui
from playsound import playsound

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
	
	#processos?
	try:
		elem_processos = driver.find_element_by_id('lbNoProcesses')
	except NoSuchElementException:  #spelling error making this code not work as expected
		print str(now)[:19] + " Existem ficheiros no GIS"
		str_ini_ficheiro = driver.find_element_by_id("dgProcesses__ctl3_Label1").text #capturar a string dentro desta tag
		print "Ficheiro no GIS desde" + str_ini_ficheiro
		
		"""
			Calcular variacao de tempo
		"""
		
		dt_ficheiro = datetime.datetime.strptime(str_ini_ficheiro, '%Y-%m-%d %H:%M:%S')
		tdelta = now - dt_ficheiro
		print "Passaram " + str(tdelta.total_seconds()) + " segundos"
		
		if tdelta.total_seconds() > 10*60:
			"""
			Necessário alarme e popup
			"""
			playsound('beep-30.wav')
			easygui.msgbox("Existe ficheiro preso no GIS  mais de 10 minutos, verifique!", title="GIS")
		
		#pass
	#<span id="dgProcesses__ctl3_Label1" >2019-08-12 13:06:49</span>
	time.sleep(60)
	#driver.submit()
	#driver.get('https://vpn.montepio.pt/+CSCO+00756767633A2F2F7367637A6261766762652E7A626167726376622E70627A++/')
	

#driver.quit()
