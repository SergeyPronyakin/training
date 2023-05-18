from datetime import datetime
from sys import maxsize


class AccountData:

    def __init__(self, firstname=None, lastname=None,
                 all_phones_from_home_page=None, mobile=None, home_phone=None,
                 work_phone=None, all_emails_from_home_page=None, email=None, email2=None, email3=None,
                 address=None, id=None, account_group_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.mobile = mobile
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.address = address
        self.id = id
        self.account_group_id = account_group_id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
            self.id, self.firstname, self.lastname, self.address, self.all_emails_from_home_page,
            self.all_phones_from_home_page, self.mobile, self.work_phone, self.home_phone,
            self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or self.firstname is None or
                self.lastname is None or other.id is None or
                self.mobile is None or self.email is None or
                self.email2 is None or self.email3 is None or
                self.work_phone is None or
                self.home_phone is None or self.address is None or
                self.id == other.id) and self.firstname == other.firstname\
            and self.lastname == other.lastname and self.mobile == other.mobile\
            and self.email == other.email and self.email2 == other.email2 and self.email3 == other.email3\
            and self.home_phone == other.home_phone and self.work_phone == other.work_phone\
            and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return int(maxsize)
