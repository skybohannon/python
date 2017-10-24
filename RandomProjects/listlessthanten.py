list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessthan10 = []

print(str(list) + '\n')
num = int(input("Enter a number to print the numbers in the list less than this: "))

for numbers in list:
    if numbers < num:
        lessthan10.append(numbers)
print(lessthan10)
