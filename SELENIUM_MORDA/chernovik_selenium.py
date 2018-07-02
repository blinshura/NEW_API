# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def test():
    driver = webdriver.Firefox()
    driver.get("https://ips1/login")
    driver.find_element_by_name("Login").clear()
    driver.find_element_by_name("Login").send_keys("demo")
    driver.find_element_by_name("Password").clear()
    driver.find_element_by_name("Password").send_keys("demo")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    t = driver.find_element_by_xpath("//div[@id='mainMenu-notification']/a/strong").text
    if t == 'demo1':
        print('!!!!')
    else:
        print('huevo')
    driver.close()
    # try:
    #     self.assertEqual("demo", driver.find_element_by_xpath("//div[@id='mainMenu-notification']/a/strong").text)
    # except AssertionError as e:
    #     self.verificationErrors.append(str(e))

test()