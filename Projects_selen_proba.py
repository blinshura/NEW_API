# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AuthAndCheckAdminPanel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(300)
        self.base_url = "https://ips1"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_11_auth_and_check_admin_panel(self):
        driver = self.driver
        driver.get("https://ips1/login")
        self.assertEqual(u"Авторизация", driver.title)
        driver.find_element_by_name("Login").clear()
        driver.find_element_by_name("Login").send_keys("demo")
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys("demo")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            self.assertEqual(u"Администратор", driver.find_element_by_css_selector("li > a > span").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        pass
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
