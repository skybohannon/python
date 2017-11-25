# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
#
#
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

num_list = [1, 2, 2]
num_list_2 = [1, 2, 1]


def has22(lst):

    for i in range(len(num_list) - 1):
        if num_list[i] ==2 and num_list[i+1] == 2:
            return True
    return False


print(has22(num_list))

