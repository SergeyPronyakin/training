import jsonpickle
import os
import string
import random

from fixture.generator_helper import GeneratorHelper
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


testdata = [GroupData(name="", footer="", header="")] + [
    GroupData(name=GeneratorHelper().random_str("name", 10), footer=GeneratorHelper().random_str("footer", 25),
              header=GeneratorHelper().random_str("header", 25))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))
