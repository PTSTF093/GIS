#!/usr/bin/python
# -*- coding: utf-8 -*-
PASSWORD = 'Tp5\'6s-7'
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

elem_p.send_keys(PASSWORD + Keys.RETURN)



#esperar um pouco
time.sleep(5)


# Verificar se password expirou
# Verificar se password expirou
# Verificar se password expirou
# Verificar se password expirou
# Verificar se password expirou
#<td nowrap="">New Password</td>
#//*[@id="form_table"]/tbody/tr[3]/td/div/table/tbody/tr[2]/td[1]
try:
	#elem_botao = driver.find_element_by_name('cmdActiveReport')
	#elem_td_expired = driver.find_element(By.XPATH, '//button[text()="Some text"]')
	elem_td_expired = driver.find_element(By.XPATH, '//*[@id="form_table"]/tbody/tr[3]/td/div/table/tbody/tr[2]/td[text()="New Password"]')
	texto_para_msg = "É necessário alterar a password para o user Z0356. A password atual é " + PASSWORD + "\nFaça a alteração agora, antes de clicar em OK neste popup e coloque a nova password no ficheiro GIS.py que se encontra no Desktop.\nEdite o ficheiro e substitua na terceira linha do ficheiro entre as plicas.\nDepois, volte a executar o GIS.py\nComunique essa alteração enviando mail para ptstf093@pt.ibm.com com a nova password."
	easygui.msgbox(texto_para_msg, title="PASSWORD")
	quit()
except NoSuchElementException:
	easygui.msgbox("PASSWORD OK")


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
	try:
		elem_botao = driver.find_element_by_name('cmdActiveReport')
	except NoSuchElementException:
		time.sleep(5)
		driver.get('https://vpn.montepio.pt/+CSCO+00756767633A2F2F7367637A6261766762652E7A626167726376622E70627A++/')
		WebDriverWait(driver, 10).until(EC.title_contains("FTPMonitor"))
		continue
	elem_botao.click()
	now = datetime.datetime.now()
	print "refresh efetuado " + str(now)[:19] #print str(now)[:19]
	#driver.execute_script("document.body.style.backgroundColor = 'red';")
	#time.sleep(5)
	#driver.execute_script("document.body.style.backgroundColor = 'white';")
	#processos?
	try:
		elem_processos = driver.find_element_by_id('lbNoProcesses')
	except NoSuchElementException:  #spelling error making this code not work as expected
		print str(now)[:19] + " Existem ficheiros no GIS"
		#str_ini_ficheiro = driver.find_element_by_id("dgProcesses__ctl3_Label1").text #capturar a string dentro desta tag
		# A pedido do Elói foi alterado Label1 para Label2 porque diz que é para considerar datahora de fim do ficheiro por causa das mudanças de estado do ficheiro.
		str_fim_ficheiro = driver.find_element_by_id("dgProcesses__ctl3_Label2").text #capturar a string dentro desta tag
		print "Ficheiro no GIS desde " + str_fim_ficheiro
		
		"""
			Calcular variacao de tempo
		"""
		
		dt_ficheiro = datetime.datetime.strptime(str_fim_ficheiro, '%Y-%m-%d %H:%M:%S')
		tdelta = now - dt_ficheiro
		print "Passaram " + str(tdelta.total_seconds()) + " segundos"
		
		if tdelta.total_seconds() > 20*60: #minutos * segundos
			"""
			Necessário alarme e popup
			"""
			playsound('beep-30.wav')
			driver.execute_script("document.body.style.backgroundColor = 'red';")
			easygui.msgbox("Existe ficheiro preso no GIS  mais de 20 minutos, verifique!", title="GIS")
			driver.execute_script("document.body.style.backgroundColor = 'white';")
		#pass
	#<span id="dgProcesses__ctl3_Label1" >2019-08-12 13:06:49</span>
	time.sleep(60)
	#driver.submit()
	#driver.get('https://vpn.montepio.pt/+CSCO+00756767633A2F2F7367637A6261766762652E7A626167726376622E70627A++/')
	

#driver.quit()
