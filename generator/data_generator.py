from model.group import Group
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f_groups = "data/groups.json"
f_contacts = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata_group = [Group(name="", header="", footer="")] + [
            Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
            for i in range(n)
]

file_group = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f_groups)

with open(file_group, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata_group))

testdata_contact = [Contact(lastname="", firstname="", address="", email="", email2="",
                    email3="", home="", work="", phone2="", mobile="")] + [
            Contact(lastname=random_string("lastname", 10),
                    firstname=random_string("firstname", 20),
                    address=random_string("address", 20),
                    email=random_string("email", 20),
                    email2=random_string("email2", 20),
                    email3=random_string("email3", 20),
                    home=random_string("home", 10),
                    work=random_string("work", 10),
                    phone2=random_string("phone2", 10),
                    mobile=random_string("mobile", 10))
            for i in range(n)
]

file_contact = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f_contacts)

with open(file_contact, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata_contact))
