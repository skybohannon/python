# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
<<<<<<< Updated upstream
# If the given string already begins with "Is" then return the string unchanged.

def new_string(s):
    if len(s) >= 2 and s[:2] == "Is":
        return s
    else:
        return "Is " + s

print(new_string("Is a cat better than a dog? No."))
print(new_string("a cat better than a dog? No."))
=======
# If the given string already begins with "Is" then return the string unchanged. Go to the editor
# Click me to see the sample solution
>>>>>>> Stashed changes
