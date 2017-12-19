# 1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different
# from each other.


def is_equal(data):
    count = 0
    for n in data:
        for j in range(1, len(data) - 1):
            if n == j:
                count += 1
                if count == 2:
                    return False


print(is_equal([2, 4, 6, 8]))
print(is_equal([2, 4, 2, 6, 8]))
