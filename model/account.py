from datetime import datetime
from sys import maxsize


class AccountData:

    def __init__(self, firstname="Firstname", middlename="Middlename",
                 lastname="Lastname", mobile="89160000101", email="test@gmail.com", id=None):
        self.firstname = firstname
        self. middlename = middlename
        self.lastname = lastname
        self.mobile = mobile
        self.email = email
        self.id = id

    def test_data(self, assert_text: str):
        test_data = assert_text + str(datetime.now())

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

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.middlename, self.lastname, self.mobile, self.email)

    def __eq__(self, other):
        return (self.id is None or self.firstname is None or self.middlename is None or
                self.lastname is None or other.id is None or
                self.mobile is None or self.email is None or self.id == other.id) and self.firstname == other.firstname\
            and self.middlename == other.middlename and self.lastname == other.lastname and self.mobile == other.mobile\
            and self.email == other.email

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return int(maxsize)
