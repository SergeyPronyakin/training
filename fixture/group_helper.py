from datetime import datetime


class GroupHelper:

    GROUP_PAGE = "http://localhost/addressbook/group.php"

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("groups").click()

    def count_of_groups(self):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("groups").click()
        return len(wd.find_elements_by_xpath("//div[4]/form/span"))

    def create_group(self, group):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("groups").click()
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

    def return_to_the_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def edit_group(self):
        assert_group_name = "Assert group name" + str(datetime.now())
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(assert_group_name)
        wd.find_element_by_name("update").click()

    def delete_group(self):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("groups").click()
        group_list = wd.find_elements_by_name("selected[]")
        if group_list:
            group_list[0].click()
            wd.find_element_by_name("delete").click()

    def delete_all_group(self):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("groups").click()
        all_groups_checkboxes = wd.find_elements_by_name("selected[]")
        for group in all_groups_checkboxes:
            group.click()
        wd.find_element_by_name("delete").click()
