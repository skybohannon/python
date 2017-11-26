# # Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.
#
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

num_array = [1, 2, 4, 4, 9]

def array_front9(lst):
    for i in range(0, 3):
        if i < len(lst) and lst[i] == 9:
            return True

    return False


print(array_front9(num_array))