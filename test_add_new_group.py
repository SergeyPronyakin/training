# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        dw = self.wd
        dw.get("http://localhost/addressbook/index.php")
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").click()
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()
        dw.find_element_by_link_text("groups").click()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys("name")
        dw.find_element_by_name("group_header").click()
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys("test1")
        dw.find_element_by_name("group_footer").click()
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys("test2")
        dw.find_element_by_name("submit").click()
        dw.find_element_by_link_text("group page").click()
        dw.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
