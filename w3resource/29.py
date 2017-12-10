# 29. Write a Python program to print out a set containing all the colors from color_list_1 which
#  are not present in color_list_2.
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}


def not_contain(lst1, lst2):
    newlst = []
    for i in lst1:
        if i in lst2:
            continue
        else:
            newlst.append(i)

    return newlst


print(not_contain(["White", "Black", "Red"], ["Red", "Green"]))
