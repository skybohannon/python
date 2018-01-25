# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


def remove_certain(l):
    new_list = [x for (i,x) in enumerate(l) if i not in (0,4,5)]
    return new_list

print(remove_certain(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
