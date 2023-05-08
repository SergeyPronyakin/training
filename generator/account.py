from model.account import AccountData
import jsonpickle
import os
import string
import random
import sys
import getopt

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


def random_str(prefix, maxlen):
    symbols = string.ascii_letters  # + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_int(min, max):
    return "".join(random.choice("0123456789") for i in range(random.randint(min, max)))


def random_phone():
    phone = []
    country_codes = [random_int(1, 2)]
    city_codes = [random_int(1, 4)]
    random_index = int(random.choice("01"))
    prefs = ["", "+"][random_index]
    parenthesis_open = ["", "("][random_index]
    phone_bodies = [random_int(4, 8)]
    for a, b, c, d, e in zip(prefs, country_codes, parenthesis_open, city_codes, phone_bodies):
        phone.append(a)
        phone.append(b)
        phone.append(c)
        phone.append(d)
        if c:
            phone.append(")")
        phone.append(e)

    return "".join(phone)


testdata2 = [AccountData(firstname="", lastname="", mobile="",
                         email="", email2="", email3="", address="",
                         home_phone="", work_phone="")] + [
                AccountData(firstname=firstname, lastname=lastname, mobile="+79161930000",
                            email=email, email2=email2, email3=email3, address=address,
                            home_phone="+77777777", work_phone="899999999")
                for firstname in ["", random_str("name", 5)]
                for lastname in ["", random_str("lastname", 5)]
                for address in ["", random_str("address", 5)]
                for email in ["", "testmail@gmail.com"]
                for email2 in ["", "testmail2@gmail.com"]
                for email3 in ["", "testmail3@gmail.com"]
            ]

testdata = [
    AccountData(firstname=random_str("name", 10), lastname=random_str("lastname", 10), mobile=random_phone(),
                email=random_str("email", 10), email2=random_str("email2", 10), email3=random_str("email3", 10),
                address=random_str("email", 30), home_phone=random_phone(), work_phone=random_phone())
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))
