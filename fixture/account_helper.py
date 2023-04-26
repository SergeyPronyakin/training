from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fixture.openers.page_opener import PageOpener
from model.account import AccountData


class AccountHelper:

    HOME_PAGE = "http://localhost/addressbook/index.php"

    def __init__(self, app):
        self.app = app
        self.page_opener = PageOpener(app)

    def input_text_in_fields(self, text, selector_name):
        wd = self.app.wd
        field = wd.find_element_by_name(selector_name)
        field.click()
        field.clear()
        field.send_keys(text)

    def create_account(self, account):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        wd.find_element_by_link_text("add new").click()
        self.input_text_in_fields(account.firstname, "firstname")
        self.input_text_in_fields(account.middlename, "middlename")
        self.input_text_in_fields(account.lastname, "lastname")
        self.input_text_in_fields(account.mobile, "mobile")
        self.input_text_in_fields(account.email, "email")
        wd.find_element_by_name("submit").click()
        return AccountData(firstname=account.firstname, middlename=account.middlename, lastname=account.lastname,
                           mobile=account.mobile, email=account.email)

    def return_to_the_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_of_accounts(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        return len(wd.find_elements_by_name("entry"))

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

    def get_account_objects(self) -> list:
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.HOME_PAGE)
        return wd.find_elements_by_name("entry")

    def get_account_ids(self) -> list:
        account_values = []
        for el in self.get_account_objects():
            account_id = el.find_element_by_name("selected[]").get_attribute("id")
            account_values.append(account_id)
        return account_values

    def get_account_attributes_text(self, xpath) -> list:
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.HOME_PAGE)
        account_attributes = wd.find_elements_by_xpath(xpath)
        account_attributes_text = []
        for el in account_attributes:
            account_attributes_text.append(el.text)
        return account_attributes_text

    def accounts(self):
        return [AccountData(firstname=firstname, lastname=lastname,
                            mobile=mobile, email=email, id=value)
                for firstname, lastname, mobile, email, value
                in zip(self.get_account_attributes_text("//td[3]"),
                       self.get_account_attributes_text("//td[2]"),
                       self.get_account_attributes_text("//td[6]"),
                       self.get_account_attributes_text("//td[5]"),
                       self.get_account_ids())]
