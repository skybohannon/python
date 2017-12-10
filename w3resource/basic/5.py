# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

user_name = input("Please enter your name: ")
name_list = user_name.split(" ")
print(name_list[1] + " " + name_list[0])