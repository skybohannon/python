birthdays = {
    "Sky Bohannon": "10/04/1983",
    "Albert Einstein": "03/14/1979",
}

print("Welcome to the birthday dictionary. We know the birthdays of: ")
for n in birthdays:
    print(n)

who = input("\nWhose birthday do you want to look up? ").title()

if who in birthdays:
    print("{}'s birthday is {}".format(who, birthdays[who]))
else:
    print("We do not have {}'s birthday".format(who))
