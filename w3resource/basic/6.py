# # Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

user_input = input("Please enter a comma-separated list of numbers: ")
user_list = user_input.split(", ")
user_tuple = tuple(user_list)
print("List: " + str(user_list) + "\nTuple: " + str(user_tuple))
