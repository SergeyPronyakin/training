from datetime import datetime


class AccountData:

    def __init__(self):
        self.firstname = "Test"
        self. middlename = "Testovich"
        self.lastname = "Testov"
        self.mobile = "891600000"
        self.email = "sp@testmail.com"

    def test_data(self):
        test_data = "Test" + str(datetime.now())

        if self.firstname:
            self.firstname = test_data
        if self.middlename:
            self.middlename = test_data
        if self.lastname:
            self.lastname = test_data
        if self.mobile:
            self.mobile = test_data
        if self.email:
            self.email = test_data

        return self
