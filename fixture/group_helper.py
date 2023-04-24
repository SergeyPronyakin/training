from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fixture.openers.page_opener import PageOpener
from model.group import GroupData


class GroupHelper:
    GROUP_PAGE = "http://localhost/addressbook/group.php"

    def __init__(self, app):
        self.app = app
        self.page_opener = PageOpener(app)

    def get_group_page(self):
        wd = self.app.wd
        return wd.get(self.GROUP_PAGE)

    def count_of_groups(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.GROUP_PAGE)
        return len(wd.find_elements_by_xpath("//div[4]/form/span"))

    def create_group(self, group) -> GroupData:
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.GROUP_PAGE, check_xpath_element="//input[@name='new']")
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
        return GroupData(name=group.name, header=group.header, footer=group.footer)

    def return_to_the_group_page(self):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'group page')))
        wd.find_element_by_link_text("group page").click()

    def edit_group(self, assert_name):
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.GROUP_PAGE, check_xpath_element="//div[4]/form")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(assert_name)
        wd.find_element_by_name("update").click()

    def delete_group(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.GROUP_PAGE, check_xpath_element="//div[4]/form")
        group_list = wd.find_elements_by_name("selected[]")
        if group_list:
            group_list[0].click()
            wd.find_element_by_name("delete").click()

    def delete_all_group(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.GROUP_PAGE, check_xpath_element="//form/input[6]")
        all_groups_checkboxes = wd.find_elements_by_name("selected[]")
        for group in all_groups_checkboxes:
            group.click()
        wd.find_element_by_name("delete").click()

    def get_group_objects(self) -> list:
        wd = self.app.wd
        self.page_opener.open_page_with_check(url=self.GROUP_PAGE, check_xpath_element="//form/input[6]")
        return wd.find_elements_by_css_selector("span.group")

    def get_group_names(self) -> list:
        group_names = []
        for group in self.get_group_objects():
            group_names.append(group.text)
        return group_names

    def get_group_values(self) -> list:
        group_values = []
        for group in self.get_group_objects():
            group_values.append(group.find_element_by_name('selected[]').get_attribute("value"))
        return group_values

    def groups(self):
        return [GroupData(name=x, id=y) for x, y in zip(self.get_group_names(), self.get_group_values())]

