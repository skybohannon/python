# # Use bubble sort to solve this problem.
# # Wiki on the algorithm at https://en.wikipedia.org/wiki/Bubble_sort
#
#
# def bubble_sort(numbers):
#     """ Use bubble sort to sort a list of numbers in ascending order.
#         Return the input list after mutating it with sorted numbers.
#
#     >>> bubble_sort([2, 19, 4, 1, -40])
#     [-40, 1, 2, 4, 19]

numlist = [54,26,93,17,77,31,44,55,20]


def bubble_sort(lst):
    for passnum in range(len(lst)-1, 0, -1):
        for i in range(passnum):
            if lst[i]>lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i+1] = temp
    return lst


print(bubble_sort(numlist))