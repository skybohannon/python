# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
#
#
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

num_list = [10, 3, 5, 6]
num_list_2 = [7, 2, 10, 9]
num_list_3 = [2, 10, 7, 2]

def big_diff(lst):
    return max(lst) - min(lst)


print(big_diff(num_list))
print(big_diff(num_list_2))
print(big_diff(num_list_3))
