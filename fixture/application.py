from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.account_helper import AccountHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group_helper = GroupHelper(self)
        self.account_helper = AccountHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False




    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")
        return wd

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True

    def quit(self):
        self.wd.quit()

