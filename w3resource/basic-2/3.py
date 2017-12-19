# 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

def remove_nums(lst):
    idx = 0
    position = 3 - 1
    len_list = len(lst)
    while len_list > 0:
        idx = (position + idx) % len_list
        print(lst.pop(idx))
        len_list -= 1

num_list = [10,20,30,40,50,60,70,80,90]
print(remove_nums(num_list))