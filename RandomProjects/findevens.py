numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenList = []
for number in numberList:
    if number % 2 == 0:
        evenList.append(number)

print("The even numbers are: " + ', '.join(str(x) for x in evenList))
