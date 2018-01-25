# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same
# from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


def count_it(l):
    counter = 0
    for x in l:
        if len(x) > 2 and x[:1] == x[-1:]:
            counter += 1
    return "Total: " + str(counter)


print(count_it(['abc', 'xyz', 'aba', '1221', '1337331']))
