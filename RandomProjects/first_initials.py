# # Write a program that takes a full name, prints the initials of the first,
# # middle, and last name. If the middle name is “NA”, then the program
# # should print only the initials of the first and the last name.
#
#
# def get_initials(name):
#     """ Return initials of first, last and middle name.
#     If the middle name is 'NA', return only the initials of the first and the last name.
#
#     >>> get_initials("Alfred E. Newman")
#     >>> 'A.E.N.'
#     >>> get_initials("John NA Smith")
#     >>> 'J.S.'
#     """

def get_initials(name):
    initial_list = []
    full_name = name
    full_name_list = full_name.split(" ")

    for name in full_name_list:
        if name == "NA":
            pass
        else:
            initial_list.append(name[:1])

    initial_string = ". ".join(initial_list).upper()+"."
    return initial_string


userName = input("~ ~ ~ LET'S GET SOME INITIALS~ ~ ~!\nPlease enter a full name: ")
print(get_initials(userName))
