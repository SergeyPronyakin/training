from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class GroupHelper:
    GROUP_PAGE = "http://localhost/addressbook/group.php"

    def __init__(self, app):
        self.app = app

    def open_group_page_with_check(self, check_url=None, check_xpath_element=None):
        """Input URL to check current URL and XPATH selector for checking it at the page"""
        wd = self.app.wd

        if not check_url:
            check_url = self.GROUP_PAGE

        # If xpath is not input
        if not check_xpath_element:
            # Do not change page if current page text is desired
            if wd.current_url == check_url:
                return
        # If xpath is input
        else:
            # Do not change page if current page text is desired and there is desired xpath selector at this page
            if check_url in wd.current_url and wd.find_elements_by_xpath(check_xpath_element):
                return

        self.get_group_page()

    def get_group_page(self):
        wd = self.app.wd
        return wd.get(self.GROUP_PAGE)

    def count_of_groups(self):
        wd = self.app.wd
        self.open_group_page_with_check()
        return len(wd.find_elements_by_xpath("//div[4]/form/span"))

    def create_group(self, group):
        wd = self.app.wd
        self.open_group_page_with_check(check_xpath_element="//input[@name='new']")
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_the_group_page()

    def return_to_the_group_page(self):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'group page')))
        wd.find_element_by_link_text("group page").click()

    def edit_group(self):
        assert_group_name = "Assert group name" + str(datetime.now())
        wd = self.app.wd
        self.open_group_page_with_check(check_xpath_element="//div[4]/form")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(assert_group_name)
        wd.find_element_by_name("update").click()

    def delete_group(self):
        wd = self.app.wd
        self.open_group_page_with_check(check_xpath_element="//div[4]/form")
        group_list = wd.find_elements_by_name("selected[]")
        if group_list:
            group_list[0].click()
            wd.find_element_by_name("delete").click()

    def delete_all_group(self):
        wd = self.app.wd
        self.open_group_page_with_check(check_xpath_element="//div[4]/form")
        all_groups_checkboxes = wd.find_elements_by_name("selected[]")
        for group in all_groups_checkboxes:
            group.click()
        wd.find_element_by_name("delete").click()
