class PageOpener:

    def __init__(self, app):
        self.app = app

    def open_page_with_check(self, url, check_xpath_element=None):
        """Input URL to check whether it is opened and XPATH selector for checking it at the page to ensure"""

        wd = self.app.wd
        # If xpath is not input
        if not check_xpath_element:
            # Do not change page if current page text is desired
            if wd.current_url == url:
                return
        # If xpath is input
        else:
            # Do not change page if current page text is desired and there is desired xpath selector at this page
            if url in wd.current_url and wd.find_elements_by_xpath(check_xpath_element):
                return

        self.app.wd.get(url)
