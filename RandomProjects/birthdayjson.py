import json
from collections import Counter

running = True

with open('birthdays.json', 'r') as f:
    birthday = json.load(f)

month_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def add_birthday():
    name = input("\nWho do you want to add to the birthday dictionary? ").title()
    date = input("What is {}'s birthday (MM/DD/YYYY)? ".format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print("{} was added to the birthday dictionary.\n".format(name))

def list_names():
    names = []
    for i in birthday:
        names = names.append(i)
    print(names)

def lookup_birthday():
    nameChoice = input("Whose birthday would you like to lookup? ").title()
    if nameChoice in birthday:
        print("{}'s birthday is {}".format(nameChoice, birthday[nameChoice]))
    else:
        print("Sorry, {} wasn't in the birthday dictionary".format(nameChoice))

def count_months():
    months = []
    for name, birthday_string in birthday.items():
        month = int(birthday_string.split("/")[0])
        months.append(month_to_string[month])
    monthDict = dict(Counter(months))

    for i in monthDict:
        print(i + ": " + str(monthDict[i]))

while running:
    choice = input("\n\t1. Add birthday\n\t2. List available names\n\t3. Lookup birthday\n\t4. Show month popularity\n\t5. Quit\n\nWhat would you like to do? ")
    if choice == "1":
        add_birthday()
    elif choice == "2":
        list_names()
    elif choice == "3":
        lookup_birthday()
    elif choice == "4":
        count_months()
    elif choice == "5":
        running = False
    else:
        print("{} wasn't a valid choice.".format(choice))