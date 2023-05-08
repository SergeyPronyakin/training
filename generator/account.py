from model.account import AccountData
import jsonpickle
import os
import sys
import getopt
from fixture.generator_helper import GeneratorHelper

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of accounts", "output file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/accounts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata2 = [AccountData(firstname="", lastname="", mobile="",
                         email="", email2="", email3="", address="",
                         home_phone="", work_phone="")] + [
                AccountData(firstname=firstname, lastname=lastname, mobile="+79161930000",
                            email=email, email2=email2, email3=email3, address=address,
                            home_phone="+77777777", work_phone="899999999")
                for firstname in ["", GeneratorHelper().random_str("name", 5)]
                for lastname in ["", GeneratorHelper().random_str("lastname", 5)]
                for address in ["", GeneratorHelper().random_str("address", 5)]
                for email in ["", "testmail@gmail.com"]
                for email2 in ["", "testmail2@gmail.com"]
                for email3 in ["", "testmail3@gmail.com"]
            ]

testdata = [
    AccountData(firstname=GeneratorHelper().random_str("name", 10), lastname=GeneratorHelper().random_str("lastname", 10),
                mobile=GeneratorHelper().random_phone(), email=GeneratorHelper().random_str("email", 10),
                email2=GeneratorHelper().random_str("email2", 10), email3=GeneratorHelper().random_str("email3", 10),
                address=GeneratorHelper().random_str("email", 30), home_phone=GeneratorHelper().random_phone(),
                work_phone=GeneratorHelper().random_phone())
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))
