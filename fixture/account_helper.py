import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fixture.openers.page_opener import PageOpener
from model.account import AccountData


class AccountHelper:
    HOME_PAGE = "http://localhost/addressbook/index.php"
    account_cache = None

    def __init__(self, app):
        self.app = app
        self.page_opener = PageOpener(app)

    def input_text_in_field(self, text, selector_name):
        wd = self.app.wd
        field = wd.find_element_by_name(selector_name)
        field.click()
        field.clear()
        field.send_keys(text)

    def get_text_from_field(self, selector_name):
        wd = self.app.wd
        field = wd.find_element_by_name(selector_name)
        return field.get_attribute("value")

    def create_account(self, account) -> AccountData:
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        wd.find_element_by_link_text("add new").click()
        self.input_text_in_field(account.firstname, "firstname")
        self.input_text_in_field(account.middlename, "middlename")
        self.input_text_in_field(account.lastname, "lastname")
        self.input_text_in_field(account.nickname, "nickname")
        self.input_text_in_field(account.address, "address")
        self.input_text_in_field(account.home_phone, "home")
        self.input_text_in_field(account.mobile, "mobile")
        self.input_text_in_field(account.work_phone, "work")
        self.input_text_in_field(account.email, "email")
        self.input_text_in_field(account.email2, "email2")
        self.input_text_in_field(account.email3, "email3")
        wd.find_element_by_name("submit").click()
        self.account_cache = None
        return AccountData(firstname=account.firstname, middlename=account.middlename, lastname=account.lastname,
                           nickname=account.nickname, address=account.address, home_phone=account.home_phone,
                           mobile=account.mobile, work_phone=account.work_phone,
                           email=account.email, email2=account.email2, email3=account.email3)

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
        self.account_cache = None

    def delete_first_account(self):
        self.delete_account_by_index(0)
        self.account_cache = None

    def delete_account_by_index(self, index):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        edit_accounts_icons = wd.find_elements_by_xpath('//img[@alt="Edit"]')
        edit_accounts_icons[index].click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.account_cache = None

    def get_edit_account_page_by_index_from_home_page(self, index):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        edit_accounts_icons = wd.find_elements_by_xpath('//img[@alt="Edit"]')
        edit_accounts_icons[index].click()

    def get_account_data_from_edit_page_by_index(self, index):
        self.get_edit_account_page_by_index_from_home_page(index)
        firstname = self.get_text_from_field("firstname")
        lastname = self.get_text_from_field("lastname")
        middlename = self.get_text_from_field("middlename")
        nickname = self.get_text_from_field("nickname")
        mobile = self.get_text_from_field("mobile")
        home_phone = self.get_text_from_field("home")
        work_phone = self.get_text_from_field("work")
        email = self.get_text_from_field("email")
        email2 = self.get_text_from_field("email2")
        email3 = self.get_text_from_field("email3")
        address = self.get_text_from_field("address")
        id = self.get_text_from_field("id")
        return AccountData(firstname=firstname, middlename=middlename, lastname=lastname,
                           nickname=nickname, address=address, home_phone=home_phone,
                           mobile=mobile, work_phone=work_phone,
                           email=email, email2=email2, email3=email3, id=id)

    def edit_some_account_by_index(self, account, index):
        wd = self.app.wd
        self.page_opener.open_page_with_check(self.HOME_PAGE)
        edit_accounts_icons = wd.find_elements_by_xpath('//img[@alt="Edit"]')
        edit_accounts_icons[index].click()

        if account.firstname:
            self.input_text_in_field(account.firstname, "firstname")
        if account.middlename:
            self.input_text_in_field(account.middlename, "middlename")
        if account.lastname:
            self.input_text_in_field(account.lastname, "lastname")
        if account.mobile:
            self.input_text_in_field(account.mobile, "mobile")
        if account.email:
            self.input_text_in_field(account.email, "email")
        if account.address:
            self.input_text_in_field(account.email, "address")

        wd.find_element_by_name("update").click()
        self.return_to_the_home_page()
        self.account_cache = None
        return AccountData(firstname=account.firstname, middlename=account.middlename, lastname=account.lastname,
                           mobile=account.mobile, email=account.email)

    def edit_first_account(self, account):
        self.edit_some_account_by_index(account, 0)

    def get_account_objects(self) -> list:
        if self.account_cache:
            return self.account_cache
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.HOME_PAGE)
        self.account_cache = wd.find_elements_by_name("entry")
        return self.account_cache

    def get_account_ids(self) -> list:
        account_ids = []
        wd = self.app.wd
        accounts = wd.find_elements_by_name("entry")
        for account in accounts:
            account_id = account.find_element_by_name("selected[]").get_attribute("id")
            account_ids.append(account_id)
        return account_ids

    def get_account_attributes_text(self, xpath):
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.HOME_PAGE)
        account_attributes = wd.find_elements_by_xpath(xpath)
        account_attributes_text = []
        for el in account_attributes:
            account_attributes_text.append(el.text)
        return account_attributes_text

    def get_accounts(self) -> list:
        lastname = self.get_account_attributes_text("//td[2]")
        firstname = self.get_account_attributes_text("//td[3]")
        address = self.get_account_attributes_text("//td[4]")
        all_emails_from_home_page = self.get_account_attributes_text("//td[5]")
        all_phones_from_home_page = self.get_account_attributes_text("//td[6]")
        ids = self.get_account_ids()

        return [AccountData(firstname=firstname, lastname=lastname, address=address,
                            all_emails_from_home_page=all_emails_from_home_page,
                            all_phones_from_home_page=all_phones_from_home_page, id=ids)
                for firstname, lastname, address, all_emails_from_home_page, all_phones_from_home_page, ids
                in zip(firstname, lastname, address, all_emails_from_home_page, all_phones_from_home_page, ids)]

    def get_count_of_accounts_from_home_page(self) -> str:
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.HOME_PAGE)
        num = WebDriverWait(wd, 5).until(
            EC.presence_of_element_located((By.ID, "search_count")))
        return num.text

    def remove_special_symbols(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_at_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.remove_special_symbols(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile, contact.work_phone]))))

    def merge_emails_like_at_home_page(self, contact):
        return "\n".join([contact.email, contact.email2, contact.email3])
