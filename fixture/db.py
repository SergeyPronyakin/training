import pymysql

from model.account import AccountData
from model.group import GroupData


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_groups(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(GroupData(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_accounts(self) -> list:
        account_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, mobile, home, work,"
                           " email, email2, email3, address from addressbook")
            for row in cursor:
                (id, firstname, lastname, mobile, home, work, email, email2, email3, address) = row
                account_list.append(AccountData(id=id, firstname=firstname, lastname=lastname,
                                                mobile=mobile, home_phone=home, work_phone=work,
                                                email=email, email2=email2, email3=email3, address=address, ))
        finally:
            cursor.close()
        return account_list


    def destroy(self):
        self.connection.close()
