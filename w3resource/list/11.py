# 11. Write a Python function that takes two lists and returns True if they have at least one common member.


def commons(l1, l2):
    result = False
    for x in l1:
        for y in l2:
            if x == y:
                result = True
                return result

print(commons([1,2,3,4,5], [5,6,7,8,9]))
print(commons([1,2,3,4,5], [6,7,8,9]))
