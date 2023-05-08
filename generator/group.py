import json
import os
import string
import random
from model.group import GroupData
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "output file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


data_group = [GroupData(name="", footer="", header="")] + [
    GroupData(name=random_str("name", 10), footer=random_str("footer", 25), header=random_str("name", 25))
    for i in range(n)
]

assert_data = [data for data in ["", random_str("Newname", 15)]]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as f_out:
    f_out.write(json.dumps(data_group, default=lambda x: x.__dict__, indent=2))
