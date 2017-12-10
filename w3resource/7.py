# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java


user_file = input("Please enter a filename: ")
user_ext = user_file.split(".")
print("The file extension is .{}".format(repr(user_ext[-1])))