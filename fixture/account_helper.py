class AccountHelper:

    def __init__(self, app):
        self.app = app

    def create_account(self, account):
        wd = self.app.wd
        self.app.open_main_page()
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

    def delete_accounts(self):
        wd = self.app.wd
        count_of_accounts = len(wd.find_elements_by_xpath('//img[@alt="Edit"]'))
        while count_of_accounts > 0:
            wd.find_element_by_xpath('//img[@alt="Edit"]').click()
            wd.find_element_by_xpath('//input[@value="Delete"]').click()
            count_of_accounts -= 1

        assert int(wd.find_element_by_id('search_count').text) == 0

    def edit_account(self):
        name = "Assert name"
        wd = self.app.wd
        wd.find_element_by_xpath('//img[@alt="Edit"]').click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(name)
        wd.find_element_by_name("update").click()
        self.return_to_the_home_page()

        # Assert first name at home page after updating
        assert wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[3]").text == name
