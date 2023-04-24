from datetime import datetime


class AccountData:

    def __init__(self, firstname=None, middlename=None, lastname=None, mobile=None, email=None):
        self.firstname = firstname
        self. middlename = middlename
        self.lastname = lastname
        self.mobile = mobile
        self.email = email

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
