import json
from collections import Counter


with open('birthdays.json', 'r') as f:
    birthday = json.load(f)

month = []
def add_birthday():
    name = input("Who do you want to add to the birthday dictionary? ").title()
    date = input("What is {}'s birthday? ".format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print("{} was added to the birthday dictionary.\n".format(name))

# add_birthday()

for i in birthday.values():
    month.append(i.split()[0])
print(month)
