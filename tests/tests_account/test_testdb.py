from fixture.orm import ORMFixture
from model.group import GroupData

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     l = db.get_contacts_in_group(GroupData(id="113"))
#     for item in l:
#         print(item)
# finally:
#     pass

try:
    l = db.get_group_list()
    for item in l:
        print(item)
finally:
    pass