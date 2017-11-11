# Sorted random floating numbers
#
# def generate_floats(start, end, how_many):
#     """ Return a list of sorted random floats in the (start, end) range.
#
#     >>> generate_floats(3, 6, 5)
#     >>> ['4.125', '4.622', '4.835', '4.981', '5.364']
#     """
import random
rounded_floats = []


def random_floats(a, b, c):
    number_list = [a, b, c]
    count = 0

    while count <= 5:
        rounded_number = round(random.uniform(min(number_list), max(number_list)), 3)
        rounded_floats.append(rounded_number)
        count += 1

    return sorted(rounded_floats)


print(random_floats(3, 6, 5))
