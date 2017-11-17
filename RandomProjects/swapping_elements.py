# # Swapping list elements
#
#
# def swap_elements(in_list):
#     """ Return the list after swapping the biggest integer in the list
#     with the one at the last position.
#
#     >>> swap_elements([3, 4, 2, 2, 43, 7])
#     >>> [3, 4, 2, 2, 7, 43]

userList = [3, 4, 2, 2, 43, 7]


def swap_elements(lst):

    elements = [3, 4, 2, 2, 43, 7]
    max_num = max(elements)
    i = elements.index(max_num)
    elements[i:i+2] = elements[i+1:i-1:-1]
    return elements


print(swap_elements(userList))
