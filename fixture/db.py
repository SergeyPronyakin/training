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
                                                email=email, email2=email2, email3=email3, address=address))
        finally:
            cursor.close()
        return account_list

    def create_account(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO addressbook (firstname, middlename, lastname, nickname, company, title, address,"
                       " home, mobile, work, fax, email, email2, email3, im, im2, im3, homepage, bday, bmonth, byear,"
                       " aday, amonth, ayear, address2,phone2, notes, deprecated ) VALUES ('AAAA', 'test2', 'test3',"
                       " 'test4', 'test4', 'test5', 'address', 'home', 'mobile','work', 'fax', 'email', 'email2',"
                       " 'email3', 'im', 'im2', 'im3', 'homepage', 10, 10, 1986, 11, 11, 2011, 'address2', 'phone2',"
                       " 'notes', 0000000)")
        self.connection.commit()
        cursor.close()

    def create_group(self):
        group_name = "group name"
        group_footer = "group footer"
        group_header = "group header"
        group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"INSERT INTO group_list(group_name, group_footer, group_header, deprecated) "
                           f"VALUES('{group_name}', '{group_footer}', '{group_header}', 00000)")
            cursor.execute('SELECT @@IDENTITY')
            for row in cursor:
                id = str(row)[1:-2]
                group.append(GroupData(id=id, name=group_name, footer=group_footer, header=group_header))
            self.connection.commit()
        finally:
            cursor.close()
        return group

    def destroy(self):
        self.connection.close()
