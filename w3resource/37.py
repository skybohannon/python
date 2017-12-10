# Write a Python program to display your details like name, age, address in three different lines.


def details(name, age, address):
    return "Name: {}\nAge: {}\nAddress: {}".format(name, str(age), address)


print(details("Sky", 34, "Alabama"))