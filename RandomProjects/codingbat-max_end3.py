# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the
# other elements to be that value. Return the changed array.#
#
# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]


def max_end3(lst):
    lstmax = max(lst[0], lst[2])
    return [lstmax, lstmax, lstmax]


print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))

