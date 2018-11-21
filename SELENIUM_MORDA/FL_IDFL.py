# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

driver = webdriver.Firefox()
LOGIN = 'demo'
PASSWORD = 'Gfd!1qaz40'
try:
        driver.get("https://ips1:888/login")
        driver.find_element_by_name("Login").clear()
        driver.find_element_by_name("Login").send_keys(LOGIN)
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys(PASSWORD)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//ul[@id='mainMenu-toolbar']/li/a/span").click()
        time.sleep(1)
        t = driver.find_element_by_xpath("//div[@id='mainMenu-notification']/a/strong").text
        if t:
            if t == LOGIN:
                print('ВОШЛИ! ПОДТВЕРДИЛИ  Лоин-' + LOGIN + '  Пароль1-' + PASSWORD)
            else:
                print('ВОШЛИ! Не подтвердили Лоин-' + LOGIN + '  Пароль2-' + PASSWORD)



        driver.find_element_by_css_selector("button.b-link").click()
        print('1')
        driver.find_element_by_name("IDFL").click()
        print('2')
        driver.find_element_by_xpath("//div[@id='content']/div[3]/form/div/div[2]/div/div/ul/li/a/span[2]").click()
        driver.find_element_by_name("SurName").clear()
        driver.find_element_by_name("SurName").send_keys(u"ПОНОМАРЕВА")
        driver.find_element_by_name("FirstName").clear()
        driver.find_element_by_name("FirstName").send_keys(u"ИРИНА")
        driver.find_element_by_name("MiddleName").clear()
        driver.find_element_by_name("MiddleName").send_keys(u"ЮРЬЕВНА")
        driver.find_element_by_name("DateOfBirth").clear()
        driver.find_element_by_name("DateOfBirth").send_keys("11.01.1966")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            unittest.TestCase().assertEqual(u"ИДЕНТПОНОМАРЕВА ИРИНА ЮРЬЕВНАв обработке...",
                             driver.find_element_by_css_selector("div.request-info").text)
        except AssertionError as e:
            unittest.TestCase().verificationErrors.append(str(e))
        driver.find_element_by_name("IDFL").click()
        driver.find_element_by_link_text(u"по паспорту").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("4004946593")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            unittest.TestCase().assertEqual(u"ИДЕНТОписание отсутствуетв обработке...",
                             driver.find_element_by_css_selector("div.request-info").text)
        except AssertionError as e:
            unittest.TestCase().verificationErrors.append(str(e))
        driver.find_element_by_name("IDFL").click()
        driver.find_element_by_link_text(u"по ОГРН / ОГРНИП / ИНН ФЛ").click()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").send_keys("782619098267")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            unittest.TestCase().assertEqual(u"ИДЕНТОписание отсутствуетв обработке...",
                             driver.find_element_by_css_selector("div.request-info").text)
        except AssertionError as e:
            unittest.TestCase().verificationErrors.append(str(e))





        driver.quit()

except:
    pass


if __name__ == "__main__":
    unittest.main()
