# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


driver = webdriver.Firefox()
EXCEPTIONs = []

def test(LOGIN, PASSWORD):

    try:

        driver.get("https://ips1:888/login")
        driver.find_element_by_name("Login").clear()
        driver.find_element_by_name("Login").send_keys(LOGIN)
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys(PASSWORD)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        t = driver.find_element_by_xpath("//div[@id='mainMenu-notification']/a/strong").text
        if t:
            if t == LOGIN:
                print('ВОШЛИ! ПОДТВЕРДИЛИ  Лоин-' + LOGIN + '  Пароль1-' + PASSWORD)
            else:
                print('ВОШЛИ! Не подтвердили Лоин-' + LOGIN + '  Пароль2-' + PASSWORD)

        driver.find_element_by_xpath("//div[@id='mainMenu-notification']/a/strong").click()
        driver.find_element_by_link_text(u"Выход").click()
    except Exception as e:
        # EXCEPTIONs.append(e)
        print( 'НЕ ВОШЛИ!!!! Лоин-' + LOGIN + '  Пароль3-' + PASSWORD)




with open('logins.txt',encoding='utf-8', newline='') as logins:
    login_pass = logins.read().split('\n')
    # print(login_pass)

a = 0
login_list = {}
for i in login_pass[::2]:
    LOGIN = str(login_pass[a])
    LOGIN = LOGIN.replace('\r', '')
    PASSWORD = str(login_pass[(a + 1)])
    PASSWORD = PASSWORD.replace('\r', '')
    #print('LOGIN:' + LOGIN + ' ' + 'PASSWORD:' + PASSWORD)
    login_list.setdefault(LOGIN, PASSWORD)
    a += 2

for l, p in login_list.items():
    LOGIN = str(l)
    PASSWORD = str(p)
    #print('LOGIN:' + l + ' ' + 'PASSWORD:' + p)
    test(LOGIN, PASSWORD)

driver.close()


print('===================================================================================')
for i in EXCEPTIONs:
    print(i)