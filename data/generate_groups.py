import string
import random
from model.group import GroupData


def random_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


group_data = [
    GroupData(name=name, footer=footer, header=header)
    for name in ["", random_str("name", 10)]
    for footer in ["", random_str("footer", 25)]
    for header in ["", random_str("name", 25)]
]

assert_data = [data for data in ["", random_str("Newname", 15)]]
