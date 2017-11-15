# # Swapping list elements
#
#
# def swap_elements(in_list):
#     """ Return the list after swapping the biggest integer in the list
#     with the one at the last position.
#
#     >>> swap_elements([3, 4, 2, 2, 43, 7])
#     >>> [3, 4, 2, 2, 7, 43]
#     """
#
#     # your code here

elements = [3, 4, 2, 43, 7]
maxNo = max(elements)
convMaxNo = maxNo -1

print(elements[4:])
for n in elements:
    if n == maxNo:
        print("booty")
        elements[4] == 77
    print(elements)

# a, b = elements.index(maxNo), elements.index(3)
# elements[b], elements[a] = elements[a], elements[b]
# print(elements)