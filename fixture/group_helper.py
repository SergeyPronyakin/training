import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fixture.openers.page_opener import PageOpener
from model.group import GroupData
from fixture.account_helper import AccountHelper


class GroupHelper:
    GROUP_PAGE = "group.php"
    group_cache = None

    def __init__(self, app):
        self.app = app
        self.page_opener = PageOpener(app)
        self.account_helper = AccountHelper(app)

    def input_text_in_fields(self, text, selector_name):
        wd = self.app.wd
        field = wd.find_element_by_name(selector_name)
        field.click()
        field.clear()
        field.send_keys(text)

    def count_of_groups(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//input[@name='new']")
        return len(wd.find_elements_by_xpath("//div[4]/form/span"))

    def create_group(self, group) -> GroupData:
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//input[@name='new']")
        wd.find_element_by_name("new").click()

        if group.name:
            self.input_text_in_fields(group.name, "group_name")
        if group.header:
            self.input_text_in_fields(group.header, "group_header")
        if group.footer:
            self.input_text_in_fields(group.footer, "group_footer")

        wd.find_element_by_name("submit").click()
        self.return_to_the_group_page()
        self.group_cache = None
        return GroupData(name=group.name, header=group.header, footer=group.footer)

    def return_to_the_group_page(self):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'group page')))
        wd.find_element_by_link_text("group page").click()

    def edit_first_group(self, assert_name, index):
        self.edit_group_by_index(assert_name, index)
        self.group_cache = None

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//div[4]/form")
        groups = wd.find_elements_by_name("selected[]")
        groups[index].click()
        wd.find_element_by_name("edit").click()

        if group.name:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)

        wd.find_element_by_name("update").click()
        self.group_cache = None
        return GroupData(id=group.id, name=group.name, header=group.header, footer=group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//div[4]/form")
        group_list = wd.find_elements_by_name("selected[]")
        if group_list:
            group_list[0].click()
            wd.find_element_by_name("delete").click()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//div[4]/form")
        group_list = wd.find_elements_by_name("selected[]")
        if group_list:
            group_list[index].click()
            wd.find_element_by_name("delete").click()
        self.group_cache = None

    def edit_group_by_id(self, group, id):
        wd = self.app.wd
        self.find_group_by_id(id).click()
        wd.find_element_by_name("edit").click()

        if group.name:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)

        wd.find_element_by_name("update").click()
        self.group_cache = None
        return GroupData(id=group.id, name=group.name, header=group.header, footer=group.footer)

    def find_group_by_id(self, id):
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//div[4]/form")
        group_list = wd.find_elements_by_name("selected[]")
        for group in group_list:
            id_group = group.get_attribute("value")
            if id_group == id:
                return group

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.find_group_by_id(id).click()
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def delete_all_group(self):
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//form/input[6]")
        all_groups_checkboxes = wd.find_elements_by_name("selected[]")
        for group in all_groups_checkboxes:
            group.click()
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def get_group_objects(self) -> list:
        if self.group_cache:
            return list(self.group_cache)
        wd = self.app.wd
        self.page_opener.open_page_with_check(part_of_url=self.GROUP_PAGE, check_xpath_element="//form/input[6]")
        self.group_cache = wd.find_elements_by_css_selector("span.group")
        return self.group_cache

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

    def get_groups(self):
        return [GroupData(name=name, id=value) for name, value in zip(self.get_group_names(), self.get_group_values())]

    def get_groups_option(self):
        groups_option_list = []
        wd = self.app.wd
        self.page_opener.open_page_with_check()
        wd.find_element_by_name("group").click()
        groups_option = wd.find_elements_by_xpath("/html/body/div/div[4]/form[1]/select/option")
        for group in groups_option:
            id = group.get_attribute("value")
            name = group.text
            groups_option_list.append(GroupData(id=id, name=name))
        print("Groups option: " + str(groups_option_list))
        return groups_option_list, groups_option

    def select_account_group(self, group_id, group_name=None):
        if group_name:
            for group in self.get_groups_option()[1]:
                if group.text == group_name:
                    group.click()

        for group in self.get_groups_option()[1]:
            id = group.get_attribute("value")
            if id == group_id:
                group.click()

    def get_add_to_option(self):
        add_to_option_list = []
        wd = self.app.wd
        self.page_opener.open_page_with_check()
        wd.find_element_by_name("to_group").click()
        add_to_option = wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/div[4]/select/option")
        for group in add_to_option:
            id = group.get_attribute("value")
            name = group.text
            add_to_option_list.append(GroupData(id=id, name=name))
        return add_to_option_list, add_to_option

    def select_add_to_option(self, group_id=None, group_name=None):
        if group_name:
            for group in self.get_add_to_option()[1]:
                print(f"group name text={group.text}")
                if group.text == group_name:
                    group.click()
                    break

        for group in self.get_add_to_option()[1]:
            id = group.get_attribute("value")
            if id == group_id:
                group.click()

        wd = self.app.wd
        self.page_opener.open_page_with_check()
        wd.find_element_by_name("add").click()

    def delete_account_from_group(self, group_id, account_id):
        wd = self.app.wd
        self.page_opener.open_page_with_check()
        self.select_account_group(group_id)
        self.account_helper.select_account_by_id(account_id)
        wd.find_element_by_name("remove").click()

