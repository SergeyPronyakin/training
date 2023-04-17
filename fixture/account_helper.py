from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from fixture.openers.page_opener import PageOpener


class AccountHelper:

    HOME_PAGE = "http://localhost/addressbook/index.php"

    def __init__(self, app):
        self.app = app
        self.page_opener = PageOpener(app)

    def create_account(self, account):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(account.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(account.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(account.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(account.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(account.email)
        wd.find_element_by_name("submit").click()

    def return_to_the_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_of_accounts(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        return len(wd.find_elements_by_xpath("//table/tbody/tr[2]"))

    def delete_all_accounts(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        count_of_accounts = len(wd.find_elements_by_xpath('//img[@alt="Edit"]'))
        while count_of_accounts > 0:
            WebDriverWait(wd, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//img[@alt="Edit"]')))
            wd.find_element_by_xpath('//img[@alt="Edit"]').click()
            wd.find_element_by_xpath('//input[@value="Delete"]').click()
            count_of_accounts -= 1

        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.ID, 'search_count')))
        assert int(wd.find_element_by_id('search_count').text) == 0

    def delete_one_account(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        wd.find_element_by_xpath('//img[@alt="Edit"]').click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()

    def edit_account(self, account):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        wd.find_element_by_xpath('//img[@alt="Edit"]').click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(account.firstname)

        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(account.email)

        wd.find_element_by_name("update").click()
        self.return_to_the_home_page()

        # New account text waiting for...
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{account.firstname}')]")))

        # Assert first name at home page after updating
        assert wd.find_element_by_xpath("//form[2]/table/tbody/tr[2]/td[3]").text == account.firstname
        assert wd.find_element_by_xpath("//form[2]/table/tbody/tr[2]/td[5]").text == account.email
