from datetime import datetime
from sys import maxsize


class AccountData:

    def __init__(self, firstname="Firstname", middlename="Middlename", lastname="Lastname", nickname="Cobra",
                 all_phones_from_home_page=None, mobile="89160000101", home_phone="8(495)7550055",
                 work_phone="+7(777)3330055", email="test@gmail.com", email2="test2@gmail.com", email3="test3@gmail.com",
                 address="Moscow, Matrosa Zheleznyaka st, 11", id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.mobile = mobile
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.address = address
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
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
            self.id, self.firstname, self.middlename, self.lastname, self.nickname,
            self.mobile, self.work_phone, self.home_phone,
            self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or self.firstname is None or self.middlename is None or
                self.lastname is None or other.id is None or
                self.mobile is None or self.email is None or
                self.email2 is None or self.email3 is None or
                self.nickname is None or self.work_phone is None or
                self.home_phone is None or self.address is None or
                self.id == other.id) and self.firstname == other.firstname and self.middlename == other.middlename\
            and self.lastname == other.lastname and self.nickname == other.nickname and self.mobile == other.mobile\
            and self.email == other.email and self.email2 == other.email2 and self.email3 == other.email3\
            and self.home_phone == other.home_phone and self.work_phone == other.work_phone\
            and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return int(maxsize)
