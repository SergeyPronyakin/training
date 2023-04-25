from datetime import datetime


class AccountData:

    def __init__(self, firstname="Firstname", middlename="Middlename",
                 lastname="Lastname", mobile="89160000101", email="test@gmail.com"):
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
