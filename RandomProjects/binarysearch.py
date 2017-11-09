def find(numList, to_find):
    for element in numList:
        if element == to_find:
            return True
    return False


l = [2, 4, 6, 8, 10]
print(find(l, 2))
print(find(l, 3))
